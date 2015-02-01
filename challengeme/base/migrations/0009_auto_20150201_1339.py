# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20150201_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='bounty',
            field=models.DecimalField(max_digits=14, decimal_places=8, default=0.0),
            preserve_default=True,
        ),
    ]
