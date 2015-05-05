from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager
from DNM.settings import MEDIA_ROOT

__author__ = 'eaura'
# gallery/models.py
from django.contrib.auth.models import *
class Album(TimeStampedModel):
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    cover_photo = models.ForeignKey('Photo', related_name='+', blank=True,
                                    null=True)
    is_public = models.BooleanField(default=True)
    date_added = models.DateField(null=True, blank=True)
    tags = TaggableManager(blank=True, help_text=None)
    order = models.PositiveIntegerField(default=9999)


class Photo(TimeStampedModel):
    def __unicode__(self):
        return self.file.url
    album = models.ForeignKey(Album)
    file = models.ImageField(upload_to='photos')
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    tags = TaggableManager(blank=True, help_text=None)