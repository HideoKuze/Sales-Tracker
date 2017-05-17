# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-15 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_remove_revenueinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenueinfo',
            name='amount_spent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
