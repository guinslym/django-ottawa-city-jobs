# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0002_job_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobref',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
