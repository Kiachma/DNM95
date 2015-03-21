__author__ = 'eaura'
# coding=utf-8
from django.db import models
from django.utils import timezone
from model_utils.managers import InheritanceManager
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from DNM.apps.members.models import *
from django.contrib.auth.models import *
from mptt.models import MPTTModel, TreeForeignKey
class KlotterPost(MPTTModel):
    def __unicode__(self):
        return self.writer + self.created.isoformat()

    text = models.TextField(verbose_name='Kommentar')
    created = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=200, verbose_name='Namn')
    member = models.ForeignKey(Member)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['-created']

    def upVotes(self):
        return KlotterVote.objects.filter(klotter=self)

    def getUpVoters(self):
        upVotes =  self.upVotes()
        users = []
        for vote in upVotes:
            users.append(vote.member)
        return users


class KlotterVote(models.Model):
    klotter = models.ForeignKey(KlotterPost)
    member = models.ForeignKey(Member)