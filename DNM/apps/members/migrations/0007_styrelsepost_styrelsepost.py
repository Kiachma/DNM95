# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_member_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='title',
            field=models.NullBooleanField(max_length=200, verbose_name='Title'),
            preserve_default=True,
        ),
    ]
