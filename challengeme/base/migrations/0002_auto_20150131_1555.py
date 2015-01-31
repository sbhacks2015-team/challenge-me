# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='bounty',
            field=models.DecimalField(decimal_places=8, max_digits=14),
            preserve_default=True,
        ),
    ]
