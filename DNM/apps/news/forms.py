from django.forms import ModelForm
from django.db import models
from django.utils import timezone
from django import forms
from datetime import timedelta
from DNM.apps.news.models import News
from django.contrib.admin.widgets import FilteredSelectMultiple
from django_summernote.widgets import SummernoteWidget

class NewsForm(ModelForm):
    class Meta:
        exclude = ('member',)
        model = News
        widgets = {
            'description': SummernoteWidget(attrs={'width': '100%'}),
        }