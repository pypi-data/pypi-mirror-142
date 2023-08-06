from django import forms


class SimpleTagWidget(forms.widgets.TextInput):
    template_name = "django/forms/widgets/tags.html"
