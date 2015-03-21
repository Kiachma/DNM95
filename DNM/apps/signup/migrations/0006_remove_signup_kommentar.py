# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20141117_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='kommentar',
        ),
    ]
