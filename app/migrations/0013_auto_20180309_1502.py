# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-09 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180309_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like_movies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Movies'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='duration',
            field=models.CharField(default=0, max_length=16),
        ),
    ]
