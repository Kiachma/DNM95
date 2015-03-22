# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20150321_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stamma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('namn', models.CharField(max_length=200, verbose_name='Titel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='stamma',
            field=models.ForeignKey(verbose_name='St\xe4mma', blank=True, to='members.Stamma', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grad',
            name='grad',
            field=models.CharField(max_length=200, verbose_name=b'Noblett'),
            preserve_default=True,
        ),
    ]
