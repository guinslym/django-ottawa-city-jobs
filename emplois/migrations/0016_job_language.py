# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0015_auto_20151230_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='language',
            field=models.CharField(max_length=2, choices=[('FR', 'Francais'), ('EN', 'English')], default='EN'),
        ),
    ]
