# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0004_auto_20151228_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salarymax',
            field=models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=11),
        ),
    ]
