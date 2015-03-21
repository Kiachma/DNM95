from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from DNM.apps.static_pages.models import PageText

__author__ = 'eaura'


@login_required
def page(request, page_id):
    text, created = PageText.objects.get_or_create(identifier=page_id)
    context = {'text': text}
    return render(request, 'simplePage.html', context)