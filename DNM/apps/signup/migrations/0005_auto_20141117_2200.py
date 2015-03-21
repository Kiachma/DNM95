# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20141117_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='avec',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
