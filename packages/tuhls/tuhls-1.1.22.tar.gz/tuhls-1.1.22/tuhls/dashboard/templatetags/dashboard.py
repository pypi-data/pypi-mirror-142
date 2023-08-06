import datetime

from django import template
from django.template import RequestContext, defaultfilters, loader
from django.urls import reverse

from tuhls.dashboard import menu

register = template.Library()


@register.simple_tag(takes_context=True)
def render_menu(context):
    return loader.get_template("dashboard/menu.html").render(
        {**context.flatten(), **{"menu": menu}}
    )


@register.simple_tag(takes_context=True)
def render_field(context: RequestContext, instance, field):
    def get_value():
        if field in context:
            return context[field]
        if "view" in context and hasattr(context["view"], field):
            return getattr(context["view"], "preview")(instance)
        if hasattr(instance, field):
            return getattr(instance, field)

    def autoformat(value):
        if isinstance(value, str):
            return value
        if isinstance(value, datetime.datetime):
            return defaultfilters.date(value) + " " + defaultfilters.time(value)
        if isinstance(value, datetime.date):
            return defaultfilters.date(value)
        if isinstance(value, datetime.time):
            return defaultfilters.time(value)

    return autoformat(get_value())


@register.simple_tag(takes_context=True)
def dashboard_url(context: RequestContext, action_name, *args, **kwargs):
    return reverse(
        context["request"].resolver_match.app_name + ":" + action_name,
        None,
        kwargs=kwargs,
    )
