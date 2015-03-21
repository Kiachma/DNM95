
__author__ = 'eaura'

from django.db import models

class PageText(models.Model):
    identifier = models.CharField(max_length=30)
    text = models.TextField(verbose_name='Text')