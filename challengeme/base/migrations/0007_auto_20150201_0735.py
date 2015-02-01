# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20150131_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='null', max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='null', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='null', max_length=40),
            preserve_default=True,
        ),
    ]
