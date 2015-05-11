# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_auto_20150511_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkbox',
            name='hidden',
            field=models.BooleanField(default=True, verbose_name=b'Kun for styret'),
            preserve_default=False,
        ),
    ]
