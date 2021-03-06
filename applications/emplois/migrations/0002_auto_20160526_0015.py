# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-26 04:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='company_desc',
            new_name='COMPANYDESC',
        ),
        migrations.RenameField(
            model_name='description',
            old_name='educationandexp',
            new_name='EDUCATIONANDEXP',
        ),
        migrations.RenameField(
            model_name='description',
            old_name='knowledge',
            new_name='KNOWLEDGE',
        ),
        migrations.RenameField(
            model_name='description',
            old_name='languagecert',
            new_name='LANGUAGECERT',
        ),
        migrations.RenameField(
            model_name='description',
            old_name='pub_date',
            new_name='POSTDATE',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='expirydate',
            new_name='EXPIRYDATE',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='jobref',
            new_name='JOBREF',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_summary',
            new_name='JOBSUMMARY',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='joburl',
            new_name='JOBURL',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='language',
            new_name='LANGUAGE',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='name',
            new_name='NAME',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='position',
            new_name='POSITION',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='pub_date',
            new_name='POSTDATE',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='salarymax',
            new_name='SALARYMAX',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='salarymin',
            new_name='SALARYMIN',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='salarytype',
            new_name='SALARYTYPE',
        ),
    ]
