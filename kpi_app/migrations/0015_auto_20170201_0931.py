# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-01 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_app', '0014_auto_20170201_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricdata',
            name='denominator',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='metricdata',
            name='numerator',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]