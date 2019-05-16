from django import template

register = template.Library()

@register.simple_tag

# If the url_param is not yet in the url,
# it will be added with value. If it is already there,
# it will be replaced by the new value.

# reference : https://djangosnippets.org/snippets/1627/

def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return  dict_.urlencode()