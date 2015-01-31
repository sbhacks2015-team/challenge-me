# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('context_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=60000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('context_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=60000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('title', models.CharField(max_length=256)),
                ('context_id', models.IntegerField(serialize=False, primary_key=True)),
                ('note', models.CharField(max_length=60000)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('goal_date', models.DateField()),
                ('bounty', models.DecimalField(max_digits=10, decimal_places=8)),
                ('challenge', models.ForeignKey(to='base.Challenge')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('context_id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instance',
            name='owner',
            field=models.ForeignKey(to='base.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to='base.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instance',
            name='supporters',
            field=models.ManyToManyField(related_name='supporters', to='base.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='challenge',
            name='charity',
            field=models.ForeignKey(to='base.Charity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='challenge',
            name='owner',
            field=models.ForeignKey(to='base.User'),
            preserve_default=True,
        ),
    ]
