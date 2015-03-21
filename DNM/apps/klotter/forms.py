from django.forms import ModelForm
from DNM.apps.klotter.models import KlotterPost
from django_summernote.widgets import SummernoteWidget
__author__ = 'eaura'


class KlotterForm(ModelForm):
    class Meta:
        exclude = ('member','parent')
        model = KlotterPost
        widgets = {
            'text': SummernoteWidget(attrs={ 'width': '100%'}),
        }