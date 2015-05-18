from django import forms
from django.core.exceptions import ValidationError

from DNM.apps.gallery.models import Album


class AlbumForm(forms.ModelForm):



    class Meta:
        fields = ['title','description']
        model = Album