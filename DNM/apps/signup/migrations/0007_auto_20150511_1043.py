# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_remove_signup_kommentar'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkbox',
            name='hidden',
            field=models.NullBooleanField(verbose_name=b'Kun for styret'),
        ),
        migrations.AddField(
            model_name='textfield',
            name='hidden',
            field=models.NullBooleanField(verbose_name=b'Kun for styret'),
        ),
        migrations.AlterField(
            model_name='checkbox',
            name='label',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'Checkbox titel', blank=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email'),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='label',
            field=models.CharField(max_length=50, verbose_name=b'Textf\xc3\xa4lt titel', blank=True),
        ),
    ]
