# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-12 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityjobs', '0002_auto_20160512_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobref',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
