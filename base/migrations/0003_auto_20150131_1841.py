# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150131_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='bitcoin_address',
            field=models.CharField(max_length=35, default='1FtQU9x78hdshngJiCBw9tbE2MYpx87eLT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charity',
            name='email',
            field=models.CharField(max_length=256, default=2),
            preserve_default=False,
        ),
    ]
