# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20150201_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='email',
            field=models.EmailField(max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='null', max_length=254),
            preserve_default=True,
        ),
    ]
