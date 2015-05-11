# coding=utf-8

from django.forms import ModelForm
from DNM.apps.signup.models import *
from DNM.apps.members.models import  Avec

from django.forms import ModelForm, ModelMultipleChoiceField
from DNM.apps.overrides.widgets import InlineCheckboxSelectMultiple
from django.forms.widgets import SelectMultiple
from django.core.exceptions import ValidationError
class SignUpForm(ModelForm):
    class Meta:
      model = SignUp
      exclude=('event','member','avec')


class TextfieldForm(ModelForm):
    class Meta:
        model = Textfield
        fields = ('label','hidden')


class CheckboxForm(ModelForm):
    class Meta:
        model = Checkbox
        fields = ('label','hidden')


class TextFieldXUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TextFieldXUserForm, self).__init__(*args, **kwargs)
        self.fields['textfield'].label = TextFieldXEvent.objects.get(pk=self.instance.textfield).label

    class Meta:
        model = TextFieldXSignup
        fields =('textfield',)


class CheckBoxXUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CheckBoxXUserForm, self).__init__(*args, **kwargs)
        self.fields['boolean'].label = CheckboxXEvent.objects.get(pk=self.instance.checkbox).label

    class Meta:
        model = CheckboxXSignUp
        fields =('boolean',)