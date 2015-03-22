# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20150321_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='post',
        ),
        migrations.RemoveField(
            model_name='title',
            name='title',
        ),
        migrations.AddField(
            model_name='title',
            name='namn',
            field=models.CharField(default=' ', max_length=200, verbose_name='Titel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='styrelsePost',
            field=models.NullBooleanField(max_length=200, verbose_name='Styrelsepost'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='title',
            field=models.ForeignKey(verbose_name='Titel', blank=True, to='members.Title', null=True),
            preserve_default=True,
        ),
    ]
