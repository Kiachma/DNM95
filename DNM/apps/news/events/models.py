# coding=utf-8
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import *
from DNM.apps.news.models import Post
from django.utils.translation import ugettext as _
__author__ = 'eaura'


class Event(Post):
    place = models.CharField(max_length=200, verbose_name=_('Plats'))
    price = models.CharField(max_length=150, verbose_name=_('Pris'))
    deadline = models.DateTimeField(verbose_name=_(u'Sista anmälningsdag'))
    date = models.DateTimeField(verbose_name=_('Datum'))
    maxSignUps = models.PositiveIntegerField(verbose_name=_('Max antal deltagare'))
    avec = models.PositiveIntegerField(default=0,verbose_name=_(u'Antal tillåt avecer'))
    madeByAdmin = models.NullBooleanField()


    def __unicode__(self):
        return self.name

    def isFull(self):
        return self.maxSignUps <= self.signup_set.all().count()

    def deadlinePassed(self):
        return self.deadline < timezone.now()

    def getCalendarDate(self):
        return self.date.strftime("%Y%m%d")

    def getLink(self):
        return HttpResponseRedirect(reverse('event:view', args=(self.id,))).url