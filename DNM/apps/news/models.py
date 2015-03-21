# coding=utf-8
from django.db import models
from model_utils.managers import InheritanceManager


__author__ = 'eaura'

from DNM.apps.members.models import *

class Post(models.Model):
    objects = InheritanceManager()
    name = models.CharField(max_length=500, verbose_name='Namn')
    description = models.TextField(verbose_name='Beskrivning')
    created = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member)
    updated = models.DateTimeField(auto_now=True)

    def getMonth(self):
        return self.created.strftime('%B')



class News(Post):
    def __unicode_Event_(self):
        return self.name