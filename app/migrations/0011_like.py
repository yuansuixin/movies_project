# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180307_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Movies')),
                ('like_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]
