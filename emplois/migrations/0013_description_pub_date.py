# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0012_auto_20151230_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
