# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_auto_20150511_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date joined'),
        ),
    ]
