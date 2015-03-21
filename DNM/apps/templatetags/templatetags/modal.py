from django import template


register = template.Library()

@register.inclusion_tag('components/ajax_modal.html')
def ajax_modal( ):
    return {

    }

