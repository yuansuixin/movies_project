# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_movies_is_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
