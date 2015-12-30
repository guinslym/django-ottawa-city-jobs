# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0013_description_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='company_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='educationandexp',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='knowledge',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='languagecert',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='salarytype',
            field=models.CharField(max_length=250, blank=True, null=True),
        ),
    ]
