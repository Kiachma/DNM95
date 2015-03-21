# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='news.Post')),
                ('place', models.CharField(max_length=200, verbose_name=b'Plats')),
                ('price', models.CharField(max_length=150, verbose_name=b'Pris')),
                ('deadline', models.DateTimeField(verbose_name=b'Sista anm\xc3\xa4lningsdag')),
                ('date', models.DateTimeField(verbose_name=b'Datum')),
                ('maxSignUps', models.PositiveIntegerField(verbose_name=b'Max antal deltagare')),
                ('madeByAdmin', models.NullBooleanField()),
            ],
            options={
            },
            bases=('news.post',),
        ),
    ]
