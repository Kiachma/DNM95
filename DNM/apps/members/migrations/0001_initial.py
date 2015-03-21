# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import sorl.thumbnail.fields
import DNM.apps.members.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=30, verbose_name='Anv\xe4ndarnamn', db_index=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'E-post')),
                ('first_name', models.CharField(max_length=200, verbose_name='F\xf6rnamn')),
                ('last_name', models.CharField(max_length=200, verbose_name=b'Efternamn')),
                ('phone', models.CharField(max_length=200, verbose_name='Telefonnummer', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name='Postadress', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text=b'Designates whether the user can log into this admin site.', verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=True, help_text=b'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name=b'active')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=DNM.apps.members.models.get_image_path, null=True, verbose_name='Profilbild', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('farg', models.CharField(max_length=20, verbose_name='F\xe4rg')),
                ('grad', models.CharField(max_length=200, verbose_name=b'Grad')),
                ('order', models.SmallIntegerField(verbose_name=b'Order')),
                ('Radsriddare', models.NullBooleanField(max_length=200, verbose_name='R\xe5dsriddare')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.CharField(max_length=200, verbose_name='\xc4mbetspost')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='grad',
            field=models.ForeignKey(default=1, to='members.Grad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='title',
            field=models.ForeignKey(verbose_name='\xc4mbetspost', blank=True, to='members.Title', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
