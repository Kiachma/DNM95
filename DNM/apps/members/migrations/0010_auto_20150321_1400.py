# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20150321_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grad',
            name='Radsriddare',
        ),
        migrations.RemoveField(
            model_name='grad',
            name='farg',
        ),
    ]
