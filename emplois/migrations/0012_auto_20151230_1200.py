# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0011_description_salarymin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='language_certificates',
            new_name='languagecert',
        ),
    ]
