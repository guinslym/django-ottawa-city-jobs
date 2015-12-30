# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0009_auto_20151230_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expirydate',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
