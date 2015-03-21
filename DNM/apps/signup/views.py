# coding=utf-8
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user

from DNM.apps.signup.forms import *
from DNM.apps.signup.models import *
from django.forms.formsets import formset_factory
from datetime import datetime
from django.utils import timezone
import pytz

def save_user_checkboxes(request, event, signup, counter):
    checkboxes = CheckboxXEvent.objects.filter(event__id=event.id)
    # checkboxes= get_check_boxes_for_event(event.id)
    for checkbox in checkboxes:
        checkboxXUser = CheckboxXSignUp()
        checkboxXUser.checkbox = checkbox
        checkboxXUser.signUp = signup
        if 'checkbox_' + str(checkbox.id) + "_" + str(counter) in request.POST:
            checkboxXUser.boolean = True
        else:
            checkboxXUser.boolean = False
        CheckboxXSignUp.save(checkboxXUser)


def save_user_text_fields(request, event, signup, counter):
    textfields = TextFieldXEvent.objects.filter(event__id=event.id)
    # checkboxes= get_check_boxes_for_event(event.id)
    for textfield in textfields:
        textFieldXUser = TextFieldXSignup()
        textFieldXUser.textfield = textfield
        textFieldXUser.signUp = signup
        if 'textfield_' + str(textfield.id) + "_" + str(counter) in request.POST:
            textFieldXUser.text = request.POST['textfield_' + str(textfield.id) + "_" + str(counter)]
            TextFieldXSignup.save(textFieldXUser)


@login_required
def Save(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = SignUpForm()
    SignUpFormSet = formset_factory(SignUpForm, )
    if request.method == 'POST':
        formset = SignUpFormSet(request.POST, request.FILES)

        if formset.is_valid():
            counter = 0
            for form in formset.forms:

                signup = form.save(commit=False)
                if(signup.name ==''):
                    counter = counter + 1
                    continue
                signup.event = event
                signup.member = get_user(request)
                if counter != 0:
                    signup.avec = True
                signup.save()
                counter = counter + 1
                save_user_checkboxes(request, event, signup, counter)
                save_user_text_fields(request, event, signup, counter)

            messages.add_message(request, messages.SUCCESS, 'Anmälan sparad')
            return HttpResponseRedirect(reverse('event:view', args=(event_id,)))

    c = {'form': form, 'event': event}
    messages.add_message(request, messages.ERROR, 'Anmälan misslyckades')
    return render(request, 'events/view.html', c)


def delete_extra_fields(signup):
    TextFieldXSignup.objects.filter(signUp=signup.id).delete()
    CheckboxXSignUp.objects.filter(signUp=signup.id).delete()


@login_required
def Remove(request, event_id, signup_id):
    signup = SignUp.objects.get(pk=signup_id)
    event = Event.objects.get(pk=event_id)
    u = request.user
    if (u.title and u.title.styrelsePost) or u.is_superuser or (u==signup.member and event.deadline>datetime.utcnow().replace(tzinfo=pytz.utc)):
        signup.delete()
        delete_extra_fields(signup)
        messages.add_message(request, messages.SUCCESS, 'Anmälan borttagen')
    else:
        messages.add_message(request, messages.ERROR, 'Du har tyvärr inte rättigheter att ta bort denna anmälan, vänligen kontakta styrelsen')
    return HttpResponseRedirect(reverse('event:view', args=(event_id,)))