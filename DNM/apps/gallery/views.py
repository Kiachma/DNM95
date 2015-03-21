# coding=utf-8
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from photologue.models import Gallery
from photologue.forms import UploadZipForm

__author__ = 'eaura'

@login_required
@user_passes_test(lambda u: u.title and u.title.styrelsePost or u.is_superuser )
def add(request):
    if request.method == 'POST':
        form = UploadZipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/photologue/gallery/")
    galleryUpload = Gallery()
    form = UploadZipForm()
    return render_to_response('gallery/add.html', {'form': form, 'galleryUpload': galleryUpload}, RequestContext(request))