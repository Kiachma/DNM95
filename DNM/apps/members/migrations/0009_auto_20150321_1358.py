# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20150321_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='title',
            field=models.NullBooleanField(max_length=200, verbose_name='Titel'),
            preserve_default=True,
        ),
    ]
