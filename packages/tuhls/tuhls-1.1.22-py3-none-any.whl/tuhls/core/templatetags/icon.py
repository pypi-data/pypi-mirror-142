from functools import cache

from django import template
from django.template.loaders.app_directories import get_app_template_dirs
from django.utils.safestring import mark_safe
from lxml import etree

register = template.Library()


@cache
def find_icon(icon_type, icon_name):
    for d in get_app_template_dirs("icons"):
        try:
            return etree.parse(f"{d}/{icon_type}/{icon_name}.svg").getroot()
        except OSError:
            pass


@register.simple_tag()
@cache
def icon(icon_name, css_class, icon_type="ho"):
    r = find_icon(icon_type, icon_name)
    if r is None:
        return "missing icon"
    r.attrib["class"] = css_class
    return mark_safe(etree.tostring(r, encoding="utf8").decode("utf8"))
