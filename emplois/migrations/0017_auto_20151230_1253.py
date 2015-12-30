# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0016_job_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='language',
            field=models.CharField(null=True, blank=True, max_length=10, default='EN'),
        ),
    ]
