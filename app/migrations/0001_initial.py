# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-05 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_password', models.CharField(max_length=32)),
                ('u_name', models.CharField(max_length=20)),
                ('u_icon', models.ImageField(upload_to='icons')),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
