# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0007_auto_20151230_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salarymax',
            field=models.DecimalField(blank=True, max_digits=11, null=True, decimal_places=2),
        ),
    ]
