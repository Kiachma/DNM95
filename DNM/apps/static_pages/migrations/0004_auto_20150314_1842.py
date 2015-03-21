# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetext',
            name='text',
            field=models.TextField(verbose_name=b'Text'),
            preserve_default=True,
        ),
    ]
