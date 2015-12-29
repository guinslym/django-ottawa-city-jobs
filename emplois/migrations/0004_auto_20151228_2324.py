# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0003_auto_20151223_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='timestamps',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='expirydate',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_summary',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobref',
            field=models.CharField(unique=True, max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='joburl',
            field=models.URLField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salarymax',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True),
        ),
    ]
