# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-12 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import tracker.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0021_auto_20170611_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedprofile',
            name='img',
            field=models.ImageField(upload_to=tracker.models.user_directory_path),
        ),
    ]
