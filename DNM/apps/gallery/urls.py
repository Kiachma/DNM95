# gallery/urls.py

from django.conf.urls import patterns, url

from DNM.apps.gallery import views


urlpatterns = patterns('',
    url(
        regex=r'^(?P<pk>\d+)/ajax-upload/$',
        view=views.AjaxPhotoUploadView.as_view(),
        name='ajax_photo_upload_view',
    ),
    url(r'^album_list/$', views.AlbumListView.as_view(), name='album_list'),
    url(r'^photolist/(?P<id>\d+)$', views.PhotoListView.as_view(), name='photo_list'),

    url(r'^album_add/$', views.AlbumCreate.as_view(), name='album_create'),
    url(r'^album_edit/(?P<pk>\d+)$', views.AlbumEdit.as_view(), name='album_edit'),
    )