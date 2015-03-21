__author__ = 'eaura'

from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

from DNM.apps.gallery.views import *


admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^add/$', add, name="add"),

)

