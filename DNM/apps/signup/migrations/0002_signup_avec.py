# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20141117_1137'),
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='avec',
            field=models.ManyToManyField(related_name='avec', verbose_name='Avecer', to='members.Avec'),
            preserve_default=True,
        ),
    ]
