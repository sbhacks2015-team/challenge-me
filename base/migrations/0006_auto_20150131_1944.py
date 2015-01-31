# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('base', '0005_auto_20150131_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=8, default=0.0, max_digits=14)),
                ('bitcoin_address', models.CharField(max_length=35)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='charity',
            name='bitcoin_address',
            field=models.CharField(max_length=35),
            preserve_default=True,
        ),
    ]
