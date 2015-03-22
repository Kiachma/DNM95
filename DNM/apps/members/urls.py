from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

from DNM.apps.members import views


admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', views.users, name='users'),
                       url(r'^(?P<user_id>\w+)$', views.profile, name='profile'),
                       url(r'^save/(?P<user_id>\w+)$', views.save, name='save'),
                       url(r'^adminSave/(?P<user_id>\w+)$', views.adminSave, name='adminSave'),
                       url(r'^delete/(?P<user_id>\w+)$', views.delete, name='delete'),
                       url(r'^admin/(?P<user_id>\w+)$', views.admin, name='admin'),
                       url(r'^kontakt/(?P<user_id>\w+)$', views.kontakt, name='kontakt'),
                       url(r'^medlem/(?P<user_id>\w+)$', views.medlem, name='medlem'),
                       url(r'^other/(?P<user_id>\w+)$', views.other, name='other'),
                       url(r'^new/$', views.new, name='new'),


                       )

