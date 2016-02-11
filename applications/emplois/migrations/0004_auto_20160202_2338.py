# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0003_job_tweeted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expirydate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
