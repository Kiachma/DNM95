# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klotter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klotterpost',
            name='text',
            field=models.TextField(verbose_name=b'Kommentar'),
            preserve_default=True,
        ),
    ]
