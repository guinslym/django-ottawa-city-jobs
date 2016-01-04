# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0018_auto_20151230_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='language',
            field=models.CharField(max_length=2, default='EN', choices=[('FR', 'Francais'), ('EN', 'English')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='timestamps',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 4, 0, 25, 12, 295685, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
