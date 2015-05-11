# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0009_auto_20150511_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkbox',
            name='hidden',
            field=models.BooleanField(verbose_name=b'Endast synlig i tabellen f\xc3\xb6r styrelsen'),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='hidden',
            field=models.BooleanField(verbose_name=b'Endast synlig i tabellen f\xc3\xb6r styrelsen'),
        ),
    ]
