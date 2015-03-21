from django import template

from django.forms import CheckboxInput
from django.forms.widgets import CheckboxSelectMultiple


register = template.Library()


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__ \
        or field.field.widget.__class__.__name__ == CheckboxSelectMultiple().__class__.__name__