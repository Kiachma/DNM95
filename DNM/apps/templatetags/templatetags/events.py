from DNM.apps.news.events.models import Event

__author__ = 'eaura'

from django import template
register = template.Library()
from django.db.models import F
from django.utils import timezone


@register.inclusion_tag('events/events.html', takes_context = True)
def getEvents(context):
    request = context['request']
    event_list = Event.objects.filter(date__gt=timezone.now()).order_by('date')

    return {'event_list': event_list,'user':request.user}
