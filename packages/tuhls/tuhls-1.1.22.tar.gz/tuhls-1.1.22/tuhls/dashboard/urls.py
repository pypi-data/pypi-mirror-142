from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test
from django.urls import include, path, reverse
from django.utils.functional import lazy

from . import views

login_forbidden = user_passes_test(
    lambda u: u.is_anonymous, lazy(reverse, str)("dashboard"), redirect_field_name=None
)

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", login_forbidden(views.login), name="login"),
    path(
        "signup/",
        login_forbidden(views.signup),
        name="signup",
    ),
    path("forgot-password/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "forgot-password/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<str:uidb64>/<str:token>",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("sign_out/", auth_views.LogoutView.as_view(), name="sign_out"),
    path("account/", views.account, name="account"),
    path("change-password/", views.change_password, name="change_password"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
