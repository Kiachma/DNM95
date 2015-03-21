# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_signup_avec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkbox',
            name='label',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Checkbox lable', blank=True),
            preserve_default=True,
        ),
    ]
