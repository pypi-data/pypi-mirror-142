from django.template.defaulttags import register


@register.simple_tag()
def lookup(dictionary, key):
    return getattr(dictionary, key)
