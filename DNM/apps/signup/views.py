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
from django.utils.translation import ugettext as _
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
        for idx,extraform in enumerate(formset.forms):
            if idx!=0:
                extraform.empty_permitted =True
        if formset.is_valid() :
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

            messages.add_message(request, messages.SUCCESS, _(u'Anmälan sparad'))
            return HttpResponseRedirect(reverse('event:view', args=(event_id,)))

    c = {'form': form, 'event': event}
    messages.add_message(request, messages.ERROR, _(u'Anmälan misslyckades'))
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
        messages.add_message(request, messages.SUCCESS, _(u'Anmälan borttagen'))
    else:
        messages.add_message(request, messages.ERROR, _(u'Du har tyvärr inte rättigheter att ta bort denna anmälan, vänligen kontakta styrelsen'))
    return HttpResponseRedirect(reverse('event:view', args=(event_id,)))

@login_required
def Edit(request, signup_id):
    u = request.user
    signup = SignUp.objects.get(pk=signup_id)
    event = signup.event
    if request.method == 'POST':
        if (u.title and u.title.styrelsePost) or u.is_superuser or (u==signup.member and event.deadline>datetime.utcnow().replace(tzinfo=pytz.utc)):


            form = SignUpForm(request.POST, instance=signup)
            signup = form.save(commit=False)
            signup.save()
            event = signup.event
            delete_extra_fields(signup)
            save_user_checkboxes(request, event, signup, 0)
            save_user_text_fields(request, event, signup, 0)
            messages.add_message(request, messages.SUCCESS, _(u'Anmälan uppdaterad'))
            return HttpResponseRedirect(reverse('event:view', args=(signup.event_id,)))
        else:
            messages.add_message(request, messages.ERROR, _(u'Du har tyvärr inte rättigheter att ta ändra denna anmälan, vänligen kontakta styrelsen'))
            return HttpResponseRedirect(reverse('event:view', args=(event.id,)))
    form = SignUpForm(instance=signup)
    event = signup.event
    event_text_fields = TextFieldXEvent.objects.filter(event_id__exact=event.id)
    event_check_boxes = CheckboxXEvent.objects.filter(event_id__exact=event.id)
    text_fields = []
    check_boxes = []
    for textfield in event_text_fields:
        tmp,_ =TextFieldXSignup.objects.get_or_create(textfield_id=textfield.id , signUp_id=signup_id)
        text_fields.append(tmp)
    for checkbox in event_check_boxes:
        tmp,_=CheckboxXSignUp.objects.get_or_create(checkbox_id=checkbox.id, signUp_id=signup_id)
        check_boxes.append(tmp)

    c = {'form': form, 'signup': signup,'check_boxes': check_boxes, 'text_fields': text_fields,}
    return render(request, 'signup/edit.html', c)