from DNM.apps.news.forms import *
from DNM.apps.news.events.models import *





class EventForm(NewsForm):
    class Meta:
        exclude = ('member','madeByAdmin')
        model = Event
        widgets = {
            'description': SummernoteWidget(attrs={ 'width': '100%'}),
             'date': forms.DateInput(format = "%m/%d/%Y %H:%M",attrs={'class':'datePicker', 'readonly':'true'}),
             'deadline': forms.DateInput(format = "%m/%d/%Y %H:%M",attrs={'class':'datePicker', 'readonly':'true'}),

        }



