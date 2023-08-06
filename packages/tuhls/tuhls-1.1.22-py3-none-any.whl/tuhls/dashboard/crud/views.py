from django.forms import models as model_forms
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from tuhls.core.forms import TailwindModelForm


class DashboardCrudMixin:
    default_form = TailwindModelForm

    def get_template_names(self):
        return [
            f"dashboard/crud/base{self.template_name_suffix}.html"
        ] + super().get_template_names()

    def get_form_class(self):
        fields = self.fields if self.fields else []
        return model_forms.modelform_factory(
            self.model, fields=fields, form=self.default_form
        )

    def get_model_name(self):
        return self.model.__name__

    def get_success_url(self):
        return reverse(self.request.resolver_match.app_name + ":list")

    slug_url_kwarg = "gid"
    slug_field = "gid"


class DashboardListView(DashboardCrudMixin, ListView):
    action_title = "List"
    ordering = ["-created_at"]
    fields = ["gid", "created_at"]


class DashboardCreateView(DashboardCrudMixin, CreateView):
    action_title = "Create"
    base_template = "dashboard/base.html"
    submit_button_caption = "Create"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DashboardUpdateView(DashboardCrudMixin, UpdateView):
    action_title = "Update"
    base_template = "dashboard/base.html"
    submit_button_caption = "Update"


class DashboardDeleteView(DashboardCrudMixin, DeleteView):
    action_title = "Delete"
    base_template = "dashboard/base.html"
    fields = []
    submit_button_caption = "Delete"

    def get_form_message(self):
        return f'Are you sure you want to delete "{self.object}"'
