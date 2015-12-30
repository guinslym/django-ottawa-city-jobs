# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0008_auto_20151230_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salarymax',
            field=models.CharField(blank=True, null=True, max_length=40),
        ),
    ]
