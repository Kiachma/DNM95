# coding=utf-8


from DNM.apps.members.models import Member, Avec
from DNM.apps.news.events.models import Event
from django.db import models

__author__ = 'eaura'


class SignUp(models.Model):
    def __unicode__(self):
        return self.event.name + '-' + self.member.get_full_name()

    member = models.ForeignKey(Member)
    name = models.CharField(max_length=200, verbose_name='Namn')
    email = models.EmailField(verbose_name='Email')
    diet = models.CharField(max_length=200, blank=True)
    event = models.ForeignKey(Event)
    created = models.DateTimeField(auto_now_add=True)
    avec =  models.NullBooleanField()


class Checkbox(models.Model):
    def __unicode__(self):
        return self.label
    hidden =models.BooleanField(verbose_name='Endast synlig i tabellen för styrelsen')
    label = models.CharField(max_length=50, blank=True, verbose_name='Checkbox titel' ,default='')


class CheckboxXEvent(models.Model):
    def __unicode__(self):
        return self.checkbox

    event = models.ForeignKey(Event)
    checkbox = models.ForeignKey(Checkbox)


class CheckboxXSignUp(models.Model):
    checkbox = models.ForeignKey(CheckboxXEvent)
    boolean = models.NullBooleanField()
    signUp = models.ForeignKey(SignUp)


class Textfield(models.Model):
    def __unicode__(self):
        return self.label
    hidden =models.BooleanField(verbose_name='Endast synlig i tabellen för styrelsen')
    label = models.CharField(max_length=50, blank=True, verbose_name='Textfält titel')


class TextFieldXEvent(models.Model):
    def __unicode__(self):
        return self.textField

    event = models.ForeignKey(Event)
    textField = models.ForeignKey(Textfield)


class TextFieldXSignup(models.Model):
    textfield = models.ForeignKey(TextFieldXEvent)
    signUp = models.ForeignKey(SignUp)
    text = models.CharField(max_length=200, blank=True)