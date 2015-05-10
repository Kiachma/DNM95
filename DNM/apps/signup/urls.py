from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

from DNM.apps.signup.views import *


admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^(?P<event_id>|None|\d+)/signup/$', Save, name='save'),
                       url(r'^(?P<signup_id>|None|\d+)/edit/$', Edit, name='edit'),
                       url(r'^(?P<signup_id>|None|\d+)/(?P<event_id>|None|\d+)/remove/$', Remove, name='remove')
)

