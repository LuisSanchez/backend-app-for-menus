from django.template.defaulttags import register


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)