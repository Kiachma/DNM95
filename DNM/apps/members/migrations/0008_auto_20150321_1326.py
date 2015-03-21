# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_styrelsepost_styrelsepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avec',
            old_name='member',
            new_name='members',
        ),
    ]
