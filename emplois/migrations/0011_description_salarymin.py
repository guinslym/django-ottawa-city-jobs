# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0010_auto_20151230_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='salarymin',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
