# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-14 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20170513_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenueinfo',
            name='total',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.ExtendedProfile'),
        ),
    ]