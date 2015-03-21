from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

from DNM.apps.news.events import views


admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^(?P<event_id>|None|\d+)/edit$', views.edit, name='edit'),
                       url(r'^(?P<event_id>\d+)/$', views.view, name='view'),
                       url(r'^(?P<event_id>|None|\d+)/delete$', views.delete, name='delete'),
                       url(r'^(?P<event_id>|None|\d+)/save/$', views.save, name='save'),
                       url(r'^$', views.all, name='all'),
)

