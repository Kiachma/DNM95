from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe

class InlineCheckboxSelectMultiple(CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        html = super(InlineCheckboxSelectMultiple, self).render(name, value, attrs, choices)
        html = html.replace('<label', '<label class="checkbox-inline"')
        html = html.replace('<li>', '')
        html = html.replace('</li>', '')
        return mark_safe(html.replace('<label', '<label class="checkbox-inline"'))