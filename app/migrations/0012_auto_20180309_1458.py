# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-09 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_movies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Movies'),
        ),
    ]
