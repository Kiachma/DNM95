from DNM.apps.news.forms import *
from DNM.apps.news.events.models import *
from functools import partial
from django.forms import DateTimeInput,DateTimeField



DateTimeInput = partial(DateTimeInput, {'class': 'datepicker'})

class EventForm(NewsForm):
    date = DateTimeField(input_formats=('%d.%m.%Y %H:%M',),widget=DateTimeInput(format="%d.%m.%Y %H:%M"))
    deadline = DateTimeField(input_formats=('%d.%m.%Y %H:%M',),widget=DateTimeInput(format="%d.%m.%Y %H:%M"))

    class Meta:
        exclude = ('member','madeByAdmin')
        model = Event
        widgets = {
            'description': SummernoteWidget(attrs={ 'width': '100%'}),

        }



