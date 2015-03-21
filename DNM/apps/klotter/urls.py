__author__ = 'eaura'

from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin


from DNM.apps.klotter.views import *

admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', klotterplanket, name="klotterplanket"),
                       url(r'^(?P<klotter_id>\d+)/$', vote, name='vote'),
                       url(r'^comment/(?P<klotter_id>\d+)/$', comment, name='comment'),
                       url(r'^new/$', new, name='new'),
                       url(r'^edit/(?P<klotter_id>\d+)/$', edit, name='edit'),
)

