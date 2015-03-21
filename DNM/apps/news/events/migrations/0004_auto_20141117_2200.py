# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20141117_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='avec',
            field=models.PositiveIntegerField(default=0, verbose_name='Antal till\xe5t avecer'),
            preserve_default=True,
        ),
    ]
