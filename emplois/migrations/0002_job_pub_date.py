# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-18 01:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 12, 18, 1, 2, 39, 514566, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
