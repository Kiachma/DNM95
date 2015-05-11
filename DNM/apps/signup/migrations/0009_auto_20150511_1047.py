# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_auto_20150511_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfield',
            name='hidden',
            field=models.BooleanField(default=True, verbose_name=b'Kun for styret'),
            preserve_default=False,
        ),
    ]
