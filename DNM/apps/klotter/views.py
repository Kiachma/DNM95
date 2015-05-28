# coding=utf-8
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from endless_pagination.decorators import page_template

from DNM.apps.klotter.forms import KlotterForm
from DNM.apps.klotter.models import KlotterPost, KlotterVote
from django.utils.translation import ugettext as _

__author__ = 'eaura'


@login_required
@page_template('klotter/klotter_page.html')  # just add this decorator
def klotterplanket(request,template='klotter.html', extra_context=None):

    if request.method == 'POST':
        form = KlotterForm(request.POST, instance=KlotterPost())
        if form.is_valid():
            klotter = form.save(commit=False)
            klotter.member = get_user(request)
            if request.POST.get("parent")!=u'None':
                parent = KlotterPost.objects.get(pk=request.POST.get("parent"))
                klotter.parent = parent
            messages.add_message(request, messages.SUCCESS, _('Kommentar sparad'))
            klotter.save()
        else:
            messages.add_message(request, messages.ERROR, _(u'Kunde inte spara inlägg. Kolla att alla obligatoriska fält är ifyllda'))

    klotter_list = [node.get_descendants(include_self=True)
         for node in KlotterPost.objects.filter(level__lte=0)]
    klotter = KlotterPost()
    if not get_user(request).grad.isGuest():
        klotter.writer = get_user(request).get_full_name
    form = KlotterForm(instance=klotter)

    context = {'nodes': klotter_list, 'form': form}
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)


@login_required
def vote(request, klotter_id):
    klotter = KlotterPost.objects.get(pk=klotter_id)
    vote, created =  KlotterVote.objects.get_or_create(member = request.user, klotter = klotter)
    if not created:
        messages.add_message(request, messages.ERROR, _(u'En röst per medlem'))
        return HttpResponseRedirect(reverse('klotter:klotterplanket'))
    else:
        vote.klotter_id=klotter_id
        KlotterVote.save(vote)
        messages.add_message(request, messages.SUCCESS, _(u'Röst sparad'))
        return HttpResponseRedirect(reverse('klotter:klotterplanket'))

@login_required
def comment(request, klotter_id):
    klotter = KlotterPost()
    if not get_user(request).grad.isGuest():
        klotter.writer = get_user(request).get_full_name
    form = KlotterForm(instance=klotter)
    context =  {'form' :form,'klotter_id':klotter_id}
    return render(request, 'klotter/writeComment.html', context)

@login_required
def new(request):
    return comment(request, None)

@login_required
def edit(request, klotter_id):
    klotter=KlotterPost.objects.get(pk=klotter_id)
    if klotter.member_id != get_user(request).id:
        messages.add_message(request, messages.ERROR, _(u'Du kan inte redigera andras inlägg'))
        return HttpResponseRedirect(reverse('klotter:klotterplanket'))

    if request.method == 'POST':
        form = KlotterForm(request.POST, instance=klotter)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _(u'Inlägg redigerat'))
        else:
            messages.add_message(request, messages.ERROR, _(u'Kunde inte spara inlägg. Kolla att alla obligatoriska fält är ifyllda'))
        return HttpResponseRedirect(reverse('klotter:klotterplanket'))

    else:

        form = KlotterForm(instance=klotter)
    context =  {'form' :form,'klotter_id':klotter_id}
    return render(request, 'klotter/editComment.html', context)