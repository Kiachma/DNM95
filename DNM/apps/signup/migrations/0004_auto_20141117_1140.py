# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20141117_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkbox',
            name='label',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'Checkbox lable', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='signup',
            name='avec',
            field=models.ManyToManyField(related_name='avec', null=True, verbose_name='Avecer', to='members.Avec', blank=True),
            preserve_default=True,
        ),
    ]
