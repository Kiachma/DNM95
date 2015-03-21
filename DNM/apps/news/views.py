# coding=utf-8
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.auth import get_user
from DNM.apps.news.models import News

from DNM.apps.news.forms import NewsForm


@login_required
@user_passes_test(lambda u: u.title and u.title.styrelsePost or u.is_superuser )
def edit(request, news_id):
    if news_id == u'None':
        news = News()
        form = NewsForm(instance=news)
        form = NewsForm()
    else:
        news = News.objects.get(pk=news_id)
        form = NewsForm(instance=news)
    return render_to_response('news/edit.html', {'form': form, 'news': news}, RequestContext(request))

@login_required
def view(request, news_id):
    news = News.objects.get(pk=news_id)
    return render_to_response('news/view.html', { 'news': news}, RequestContext(request))

@login_required
@user_passes_test(lambda u: u.title and u.title.styrelsePost or u.is_superuser )
def save(request, news_id):
    if request.method == 'POST':
        if news_id == u'None':
            form = NewsForm(request.POST)
        else:
            news = News.objects.get(pk=news_id)
            form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.member=get_user(request)
            news.save()
            messages.add_message(request, messages.SUCCESS, 'Nyhet sparad')
            return render_to_response('news/view.html', {'news': news}, RequestContext(request))
    else:
        form = NewsForm
    news=News()
    c = {'form': form,'news': news}
    messages.add_message(request, messages.ERROR, 'Åtgärden misslyckades')
    return render_to_response('news/edit.html', c, RequestContext(request))


@login_required
@user_passes_test(lambda u: u.title or u.is_superuser )
def delete(request, news_id):
    news = News.objects.get(pk=news_id)
    News.delete(news)
    messages.add_message(request, messages.SUCCESS, 'Nyhet borttagen')
    return HttpResponseRedirect(reverse('base'))


