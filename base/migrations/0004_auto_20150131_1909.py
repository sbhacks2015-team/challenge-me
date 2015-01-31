# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150131_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='bitcoin_address',
            field=models.CharField(max_length=35, default='1FtQU9X78hdshngJiCBw9tbE2MYpx87eLT'),
            preserve_default=True,
        ),
    ]
