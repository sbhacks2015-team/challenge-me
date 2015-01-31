# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20150131_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='balance',
            field=models.DecimalField(max_digits=14, default=0.0, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='balance',
            field=models.DecimalField(max_digits=14, default=0.0, decimal_places=8),
            preserve_default=True,
        ),
    ]
