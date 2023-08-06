from crispy_forms.helper import FormHelper
from crispy_forms.layout import BaseInput
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)


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


class TailwindFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "grid grid-cols-1 gap-y-6"
        self.helper.label_class = "block text-sm font-medium text-gray-700 mb-1"


class TailwindForm(TailwindFormMixin, forms.Form):
    pass


class TailwindModelForm(TailwindFormMixin, ModelForm):
    pass
