# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20141116_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avec',
            old_name='avec',
            new_name='member',
        ),
        migrations.AlterField(
            model_name='avec',
            name='diet',
            field=models.CharField(max_length=200, null=True, verbose_name='Diet', blank=True),
            preserve_default=True,
        ),
    ]
