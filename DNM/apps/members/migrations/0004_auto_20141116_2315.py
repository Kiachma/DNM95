# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20141116_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='avec',
        ),
        migrations.AddField(
            model_name='avec',
            name='avec',
            field=models.ForeignKey(verbose_name='Avec', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
