# gallery/views.py

from django.views.generic import View, ListView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from braces.views import (
    AjaxResponseMixin,
    JSONResponseMixin,
    LoginRequiredMixin,
    SuperuserRequiredMixin,
)

from DNM.apps.gallery.models import Album, Photo
from DNM.apps.gallery.forms import AlbumForm

class AlbumCreate(CreateView):
    form_class = AlbumForm
    success_url = '/gallery/album_list/'
    template_name = 'gallery/album_new.html'


class AlbumEdit(UpdateView):
    form_class = AlbumForm
    success_url = '/gallery/album_list/'
    template_name = 'gallery/album_edit.html'
    def get_queryset(self,**kwargs):
           # query_set = super(ModelxUpdateView, self).get_queryset().filter(user=self.request.user)
           query_set = Album.objects.filter(pk=self.kwargs['pk'])
           return query_set

class AlbumListView(ListView):

    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PhotoListView(ListView):

    model = Photo


    def get_queryset(self, **kwargs):
        return Photo.objects.filter(album=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(PhotoListView, self).get_context_data(**kwargs)
        album = Album.objects.get(pk=self.kwargs['id'])
        context['album'] = album
        context['now'] = timezone.now()
        return context

class AjaxPhotoUploadView(LoginRequiredMixin,
                    SuperuserRequiredMixin,
                    JSONResponseMixin,
                    AjaxResponseMixin,
                    View):
    """
    View for uploading photos via AJAX.
    """
    def post_ajax(self, request, *args, **kwargs):
        try:
            album = Album.objects.get(pk=kwargs.get('pk'))
        except Album.DoesNotExist:
            error_dict = {'message': 'Album not found.'}
            return self.render_json_response(error_dict, status=404)

        uploaded_file = request.FILES['file']
        photo = Photo.objects.create(album=album, file=uploaded_file)
        photo.save()
        response_dict = {
            'message': 'File uploaded successfully!',
        }

        return self.render_json_response(response_dict, status=200)


