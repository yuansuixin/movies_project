# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='u_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
