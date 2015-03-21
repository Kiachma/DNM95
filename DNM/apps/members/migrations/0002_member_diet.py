# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='diet',
            field=models.CharField(max_length=500, null=True, verbose_name='Diet', blank=True),
            preserve_default=True,
        ),
    ]
