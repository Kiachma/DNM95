# coding=utf-8

from django.forms import ModelForm, CharField, PasswordInput, Select, Textarea,DateInput
from DNM.apps.overrides.widgets import InlineCheckboxSelectMultiple
from DNM.apps.members.models import *
from widgets import AdvancedFileInput
from django.forms.models import inlineformset_factory
__author__ = 'eaura'
from functools import partial
DateInput = partial(DateInput, {'class': 'datepicker'})

class MemberForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['username'].widget.attrs['readonly'] = True

            self.fields.update({
            'newPass': CharField(widget=PasswordInput(),required=False),
                 })
            self.fields['password'].label = u"Lösenord för att bekräfta ändringar"
            self.fields['newPass'].label = "Nytt password"


    class Meta:
        model = Member
        fields = (
        'username', 'first_name', 'last_name','stamma' ,'email' , 'grad', 'diet','phone', 'address','password')

        widgets = {
            'password': PasswordInput(),
            'grad': Select(),
            'address': Textarea(attrs={'cols': 80, 'rows': 5}),
            'die': Textarea(attrs={'cols': 80, 'rows': 3}),
            'stamma': Select()
        }

class MemberFormMedlem(ModelForm):

    class Meta:
        model = Member
        fields = ('grad','title','stamma')

        widgets = {
            'grad': Select(),
            'title': Select(),
            'stamma': Select(),
        }

class MemberFormKontakt(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberFormKontakt, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['username'].widget.attrs['readonly'] = True

            self.fields.update({
            'newPass': CharField(widget=PasswordInput(),required=False),
                 })
            self.fields['password'].label = u"Lösenord för att bekräfta ändringar"
            self.fields['newPass'].label = "Nytt password"


    class Meta:
        model = Member
        fields = (
        'username', 'first_name', 'last_name', 'birthday','email' ,'phone', 'address','password')

        widgets = {
            'password': PasswordInput(),
            'address': Textarea(attrs={'cols': 80, 'rows': 5}),
            'birthday':DateInput()
        }



class MemberFormOther(ModelForm):

    class Meta:
        model = Member
        fields = ('diet',)

class MemberFormSuper(ModelForm):
    class Meta:
        model = Member
        fields = ('title', 'grad' )
        widgets = {
            'title': Select(),
            'grad': Select()
        }

class AvecForm(ModelForm):

    class Meta:
        model = Avec
        fields = ('name','email','diet')