# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20141117_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateTimeField(null=True, verbose_name=b'F\xc3\xb6delsetid'),
            preserve_default=True,
        ),
    ]
