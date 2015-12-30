# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0005_auto_20151229_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salarymax',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
