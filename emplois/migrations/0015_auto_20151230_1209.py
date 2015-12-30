# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0014_auto_20151230_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='timestamps',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 12, 30, 17, 9, 51, 40992, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
