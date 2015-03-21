# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_diet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Namn')),
                ('diet', models.CharField(max_length=200, verbose_name='Diet')),
                ('email', models.CharField(max_length=200, verbose_name='E-post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='avec',
            field=models.ForeignKey(verbose_name='Avec', blank=True, to='members.Avec', null=True),
            preserve_default=True,
        ),
    ]
