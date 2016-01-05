# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0002_auto_20160105_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salarymax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='job',
            name='salarytype',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
