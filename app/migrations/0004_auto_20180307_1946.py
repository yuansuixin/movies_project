# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='like_num',
            field=models.IntegerField(default=0, max_length=16),
        ),
    ]