# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='context_id',
        ),
        migrations.RemoveField(
            model_name='charity',
            name='context_id',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='context_id',
        ),
        migrations.AddField(
            model_name='challenge',
            name='id',
            field=models.AutoField(auto_created=True, serialize=False, verbose_name='ID', default=1, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charity',
            name='id',
            field=models.AutoField(auto_created=True, serialize=False, verbose_name='ID', default=1, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instance',
            name='id',
            field=models.AutoField(auto_created=True, serialize=False, verbose_name='ID', default=1, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='challenge',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='instance',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='supporters',
            field=models.ManyToManyField(related_name='supporters', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
