from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from tuhls.core.utils import AuthenticatedHttpRequest, ip_to_country, request_to_ip

from . import forms


def login(request):
    form = AuthenticationForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid() and form.clean():
            auth.login(request, form.get_user())
            return redirect("dashboard")

        messages.error(request, ["Login failed!", "Username or password not correct"])

    return render(request, "auth/login.html", {"form": form})


class PasswordResetView(auth_views.PasswordResetView):
    form_class = forms.PasswordResetForm
    template_name = "password_reset_form.html"
    email_template_name = "password_reset_email.html"


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "password_reset_done.html"


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "password_reset_confirm.html"
    post_reset_login = True
    form_class = forms.SetPasswordForm
    success_url = reverse_lazy("dashboard")


def signup(request):
    country_code = ip_to_country(request_to_ip(request))

    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            auth.login(
                request,
                auth.authenticate(
                    email=form.cleaned_data.get("email"),
                    password=form.cleaned_data.get("password"),
                ),
            )
            return redirect("dashboard")
        else:
            messages.error(request, ["Signup failed!", "Please correct the errors."])
    else:
        form = forms.SignupForm(initial={"country": country_code})

    return render(request, "auth/signup.html", {"form": form})


@login_required()
def dashboard(request: AuthenticatedHttpRequest):
    return render(
        request,
        "dashboard/dashboard.html",
        {
            "token": request.user.get_token(),
            "user": request.user,
        },
    )


@login_required()
def account(request):
    if request.method == "POST":
        form = forms.AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = forms.AccountForm(instance=request.user)

    return render(request, "dashboard/account.html", {"form": form})


@login_required()
def change_password(request):
    if request.method == "POST":
        form = forms.CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("change_password")
        else:
            messages.error(
                request, ["Password change failed!", "Please correct the errors."]
            )
    else:
        form = forms.CustomPasswordChangeForm(request.user)
    return render(request, "dashboard/change_password.html", {"form": form})
