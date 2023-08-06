from crispy_forms.helper import FormHelper
from crispy_forms.layout import BaseInput, ButtonHolder, Field, Fieldset, Layout, Row
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django_countries import countries
from django_q.tasks import async_task

from tuhls.core.forms import TailwindFormMixin, TailwindModelForm


class Button(BaseInput):
    input_type = "submit"

    def __init__(self, *args, **kwargs):
        self.field_classes = (
            "inline-flex justify-center py-3 px-6 border border-transparent shadow-sm text-base font-medium"
            + "rounded-md text-white bg-pc-600 hover:bg-pc-700 focus:outline-none focus:ring-2"
            + "focus:ring-offset-2 focus:ring-pc-500"
        )
        super().__init__(*args, **kwargs)


class EmptyChoiceField(forms.ChoiceField):
    def __init__(
        self,
        choices=(),
        empty_label=None,
        required=True,
        widget=None,
        label=None,
        initial=None,
        help_text=None,
        *args,
        **kwargs
    ):

        # prepend an empty label if it exists (and field is not required!)
        if not required and empty_label is not None:
            choices = tuple([("", empty_label)] + list(choices))

        super().__init__(
            choices=choices,
            required=required,
            widget=widget,
            label=label,
            initial=initial,
            help_text=help_text,
            *args,
            **kwargs
        )


class ButtonFullWidth(BaseInput):
    input_type = "submit"

    def __init__(self, *args, **kwargs):
        self.field_classes = (
            "w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm"
            + "font-medium text-white bg-pc-600 hover:bg-pc-700 focus:outline-none focus:ring-2"
            + "focus:ring-offset-2 focus:ring-pc-500"
        )
        super().__init__(*args, **kwargs)


class TailwindForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "grid grid-cols-1 gap-y-6"
        self.helper.label_class = "block text-sm font-medium text-gray-700 mb-1"


class PasswordResetForm(auth_forms.PasswordResetForm):
    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = "".join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, "text/html")

        async_task(email_message.send)


class SetPasswordForm(TailwindForm):
    new_password = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            "new_password",
            ButtonHolder(ButtonFullWidth("submit", "Change my Password")),
        )

    def clean_new_password(self):
        password = self.cleaned_data.get("new_password")
        password_validation.validate_password(password, self.user)
        return password

    def save(self, commit=True):
        password = self.cleaned_data["new_password"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class SignupForm(TailwindModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput(render_value=True)
    )

    news = forms.BooleanField(
        label="Receive important maintenance and service notifications",
        initial=True,
        required=False,
    )

    tos = forms.BooleanField(
        label=(
            "I have read and agree to the Terms & Conditions, Privacy Policy and Service Agreement "
            + "of this website and service."
        ),
        error_messages={
            "required": "You have to accept the Terms & Conditions, Privacy Policy and Service agreement."
        },
        initial=False,
        required=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "tos",
            "news",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper.layout = Layout(
            Fieldset(
                "Account Details",
                "email",
                "password",
            ),
            Fieldset(
                "Legal",
                Field("news", template="crispy/checkboxfield.html"),
                Field("tos", template="crispy/checkboxfield.html"),
                css_class="text-justify block",
            ),
            ButtonHolder(ButtonFullWidth("submit", "Sign Up", css_class="mt-4")),
        )

    def save(self, commit=True) -> get_user_model():
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AccountForm(TailwindModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    address = forms.CharField(required=False)
    postal_code = forms.CharField(required=False)
    country = forms.ChoiceField(
        required=False, widget=forms.Select(), choices=countries
    )
    state = forms.CharField(required=False)
    city = forms.CharField(required=False)

    company_name = forms.CharField(required=False)
    company_website = forms.CharField(required=False)
    company_vat = forms.CharField(required=False)

    news = forms.BooleanField(
        label="Receive important maintenance and service notifications",
        initial=True,
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "address",
            "postal_code",
            "country",
            "state",
            "city",
            "company_name",
            "company_website",
            "company_vat",
            "news",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Fieldset(
                "Billing Details",
                Row(
                    Field("first_name", template="crispy/field.html"),
                    Field("last_name", template="crispy/field.html"),
                    css_class="flex gap-2",
                ),
                "address",
                Row(
                    Field("postal_code", template="crispy/field.html"),
                    Field("city", template="crispy/field.html"),
                    css_class="flex gap-2",
                ),
                Field("country", template="crispy/field.html"),
                "state",
            ),
            Fieldset(
                "Company Details",
                "company_name",
                "company_website",
                "company_vat",
            ),
            Fieldset(
                "Legal",
                Field("news", template="crispy/checkboxfield.html"),
                css_class="text-justify block",
            ),
            ButtonHolder(ButtonFullWidth("submit", "Submit", css_class="mt-4")),
        )


class CustomPasswordChangeForm(TailwindFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            "old_password",
            "new_password1",
            "new_password2",
            ButtonHolder(ButtonFullWidth("submit", "Submit", css_class="mt-4")),
        )
