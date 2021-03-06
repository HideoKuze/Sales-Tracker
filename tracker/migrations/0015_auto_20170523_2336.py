# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-24 03:36
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_auto_20170515_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedprofile',
            name='amount_spent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='revenueinfo',
            name='total_amount_spent',
            field=models.DecimalField(decimal_places=2, default=Decimal('556.00'), max_digits=6, verbose_name='Total User Revenue'),
        ),
    ]
