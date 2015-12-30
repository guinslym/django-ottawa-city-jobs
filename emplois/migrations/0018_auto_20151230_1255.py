# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0017_auto_20151230_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='timestamps',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
    ]
