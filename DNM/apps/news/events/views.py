# coding=utf-8
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user

from django.contrib import messages
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from icalendar import Calendar, Event as CalEvent
from django.http import HttpResponse
from django.contrib.sites.models import Site

from DNM.apps.news.events.forms import *
from DNM.apps.signup.forms import *
from DNM.apps.signup.models import *
import itertools
from django.db.models import Q

def get_check_boxes_for_event(event_id):
    checkbox_x_events = CheckboxXEvent.objects.filter(event__id=event_id)
    checkBox_ids = []
    for checkbox_x_event in checkbox_x_events:
        checkBox_ids.append(checkbox_x_event.checkbox.id)
    return Checkbox.objects.filter(pk__in=checkBox_ids)


def get_text_fields_for_event(event_id):
    text_field_x_events = TextFieldXEvent.objects.filter(event__id=event_id)
    text_field_ids = []
    for text_field_x_event in text_field_x_events:
        text_field_ids.append(text_field_x_event.textField.id)
    return Textfield.objects.filter(pk__in=text_field_ids)


@login_required
def edit(request, event_id):
    if event_id == u'None':
        TextfieldFormSet = formset_factory(TextfieldForm, extra=1, can_delete=True)
        CheckboxFormSet = formset_factory(CheckboxForm, extra=1, can_delete=True)
        event = Event()
        form = EventForm()
        check_box_form_set = CheckboxFormSet(prefix='checkboxes')
        text_field_form_set = TextfieldFormSet(prefix='textFields')
    else:
        TextfieldFormSet = modelformset_factory(Textfield, form=TextfieldForm, extra=1, can_delete=True)
        CheckboxFormSet = modelformset_factory(Checkbox, form=CheckboxForm, extra=1, can_delete=True)
        event = Event.objects.get(pk=event_id)
        form = EventForm(instance=event)
        checkBoxes = get_check_boxes_for_event(event_id)
        textboxes = get_text_fields_for_event(event_id)

        check_box_form_set = CheckboxFormSet(prefix='checkboxes', queryset=checkBoxes)
        text_field_form_set = TextfieldFormSet(prefix='textFields', queryset=textboxes)

    if event.id is None or request.user == event.member or  (request.user.title and request.user.title.styrelsePost) or request.user.is_superuser:
        return render_to_response('events/edit.html',
                                  {'form': form, 'event': event, 'textfieldFormSet': text_field_form_set,
                                   'checkboxFormSet': check_box_form_set}, RequestContext(request))
    messages.add_message(request, messages.ERROR, 'Du har inte rätt att editera detta event')
    return HttpResponseRedirect(reverse('base', args=()))


@login_required
def view(request, event_id):
    iterator = itertools.count()

    event = Event.objects.get(pk=event_id)
    SignUpFormSet = formset_factory(SignUpForm, extra=event.avec + 1, max_num=event.avec + 1)
    if not event.visibleFor(request.user.grad.id) and not request.user.is_superuser:
        messages.add_message(request, messages.ERROR, 'Du har inte rätt att se detta event')
        return HttpResponseRedirect(reverse('base', args=()))

    signUps = SignUp.objects.filter(event=event).order_by('created')
    signUp = SignUp()
    if not get_user(request).grad.isGuest():
        signUp.name = get_user(request).get_full_name
        signUp.email = get_user(request).email
        signUp.diet = get_user(request).diet

    # form = SignUpForm(instance=signUp)

    initialData = [
        {'name': get_user(request).get_full_name,
         'email':get_user(request).email,
         'diet':get_user(request).diet,
         }
    ]
    avecs = Avec.objects.filter(members_id=get_user(request).id)
    for i in range(min(event.avec,len(avecs))):
        avec = avecs[i]
        info =  {'name': avec.name,
         'email':avec.email,
         'diet':avec.diet,
         }
        initialData.append(info)
    formset = SignUpFormSet(initial=initialData)
    check_boxes = CheckboxXEvent.objects.filter(event_id__exact=event.id)
    text_fields = TextFieldXEvent.objects.filter(event_id__exact=event.id)
    sign_up_text_fields = TextFieldXSignup.objects.filter(signUp__event=event_id)
    sign_up_check_boxes = TextFieldXSignup.objects.filter(signUp__event=event_id)

    count = {}
    count['avec'] = len(signUps.filter(avec=True))
    count['member'] = len(signUps.filter(Q(avec=False) | Q(avec__isnull=True)))

    c = {'event': event, 'signUps': signUps, 'formset': formset, 'check_boxes': check_boxes, 'text_fields': text_fields,
         'sign_up_text_fields': sign_up_text_fields, 'sign_up_check_boxes': sign_up_check_boxes, 'iterator': iterator, 'count' : count}
    return render_to_response('events/view.html', c, RequestContext(request))


def save_text_fields(event, text_field_form_set):
    for textfield in text_field_form_set:
        if textfield.instance.label != '':
            textfield = textfield.save()
            text_field_event, created = TextFieldXEvent.objects.get_or_create(event=event, textField=textfield)
            text_field_event.event = event
            text_field_event.textField = textfield
            text_field_event.save()

    for form in text_field_form_set.deleted_forms:
        if form.instance.id is not None:
            TextFieldXEvent.objects.filter(textField=form.instance.id).delete()
            TextFieldXSignup.objects.filter(textfield=form.instance.id).delete()
            Textfield.delete(form.instance)


def save_check_box(event, check_box_form_set):
    for check_box in check_box_form_set:
        if check_box.instance.label != '':
            check_box = check_box.save()
            check_box_event, created = CheckboxXEvent.objects.get_or_create(event=event, checkbox=check_box)
            check_box_event.event = event
            check_box_event.checkbox = check_box
            check_box_event.save()
    for form in check_box_form_set.deleted_forms:
        if form.instance.id is not None:
            CheckboxXEvent.objects.filter(checkbox=form.instance.id).delete()
            CheckboxXSignUp.objects.filter(checkbox=form.instance.id).delete()
            Checkbox.delete(form.instance)


@login_required
def save(request, event_id):
    if request.method == 'POST':
        if event_id == u'None' or event_id == u'':
            event = Event()
            event.madeByAdmin = hasattr(request.user, 'title')
            form = EventForm(request.POST, instance=event)
            TextfieldFormSet = formset_factory(TextfieldForm, can_delete=True)
            CheckboxFormSet = formset_factory(CheckboxForm, can_delete=True)
            check_box_form_set = CheckboxFormSet(request.POST, request.FILES, prefix='checkboxes')
            text_field_form_set = TextfieldFormSet(request.POST, request.FILES, prefix='textFields')
        else:
            event = Event.objects.get(pk=event_id)
            form = EventForm(request.POST, instance=event)
            check_boxes = get_check_boxes_for_event(event_id)
            text_boxes = get_text_fields_for_event(event_id)
            TextFieldFormSet = modelformset_factory(Textfield, form=TextfieldForm, can_delete=True)
            CheckBoxFormSet = modelformset_factory(Checkbox, form=CheckboxForm, can_delete=True)
            text_field_form_set = TextFieldFormSet(request.POST, request.FILES, queryset=text_boxes,
                                                   prefix='textFields')
            check_box_form_set = CheckBoxFormSet(request.POST, request.FILES, queryset=check_boxes, prefix='checkboxes')
        if not (
                                event.id is None or request.user == event.member or (request.user.title and request.user.title.styrelsePost) or request.user.is_superuser):
            messages.add_message(request, messages.ERROR, 'Du har inte rätt att spara detta event')
            return HttpResponseRedirect(reverse('index', args=()))
        if form.is_valid() and text_field_form_set.is_valid() and check_box_form_set.is_valid():
            event = form.save(commit=False)
            event.member = get_user(request)
            event.save()
            form.save_m2m()
            save_text_fields(event, text_field_form_set)
            save_check_box(event, check_box_form_set)
            messages.add_message(request, messages.SUCCESS, 'Evenemang sparat')
            return HttpResponseRedirect(reverse('event:view', args=(event.id,)))
    else:
        form = EventForm
    event = Event()
    c = {'form': form, 'event': event}
    messages.add_message(request, messages.ERROR, 'Åtgärden misslyckades')
    return render_to_response('events/edit.html',
                              {'form': form, 'event': event, 'textfieldFormSet': text_field_form_set,
                               'checkboxFormSet': check_box_form_set}, RequestContext(request))


@login_required
@user_passes_test(lambda u: u.title and u.title.styrelsePost or u.is_superuser)
def delete(request, event_id):
    event = Event.objects.get(pk=event_id)
    if not (request.user == event.member or (request.user.title and request.user.title.styrelsePost) or request.user.is_superuser):
        messages.add_message(request, messages.ERROR, 'Du har inte rätt att ta bort detta event')
        return HttpResponseRedirect(reverse('index', args=()))
    Event.delete(event)
    messages.add_message(request, messages.SUCCESS, 'Evenemang borttaget')
    return HttpResponseRedirect(reverse('base'))


def all(request):
    event_list = Event.objects.all().order_by('date')
    c = {'event_list': event_list}
    return render_to_response('events/all.html', c, RequestContext(request))


def export(request):
    event_list = Event.objects.filter()

    cal = Calendar()
    site = Site.objects.get_current()

    cal.add('prodid', '-//%s Events Calendar//%s//' % (site.name, site.domain))
    cal.add('version', '2.0')

    site_token = site.domain.split('.')
    site_token.reverse()
    site_token = '.'.join(site_token)
    for event in event_list:
        ical_event = CalEvent()
        if event.madeByAdmin:
            ical_event.add('name', event.name)
        else:
            ical_event.add('name', event.name + ' (' + event.member.get_full_name() + ')')
        ical_event.add('summary', event.name)
        ical_event.add('dtstart', event.date)
        ical_event.add('location', event.place)
        ical_event.add('description', event.description)
        # ical_event.add('dtstamp', event.end and event.end or event.start)
        ical_event['uid'] = '%d.event.events.%s' % (event.id, site_token)
        cal.add_component(ical_event)
        calString = unicode(cal.to_ical(), "utf-8")
    response = HttpResponse(calString, content_type="text/calendar; charset=UTF-8")
    response['Content-Disposition'] = 'attachment; filename=%s.ics' % 'ics'
    return response