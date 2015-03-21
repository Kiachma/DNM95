__author__ = 'eaura'
from django.forms import ModelForm
from photologue.models import Gallery


class UploadZipForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadZipForm, self).__init__(*args, **kwargs)
        self.fields['zip_file'].label = 'Zip fil'
        self.fields['title'].label = 'Titel'
        self.fields['caption'].label = 'Bildtext'
        self.fields['description'].label = 'Beskrivning'

    class Meta:
        exclude = ('gallery', 'tags', 'is_public')
        model = Gallery

