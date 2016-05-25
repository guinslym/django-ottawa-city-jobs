# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KNOWLEDGE', models.TextField(blank=True, null=True)),
                ('LANGUAGE_CERTIFICATES', models.TextField(blank=True, null=True)),
                ('EDUCATIONANDEXP', models.TextField(blank=True, null=True)),
                ('COMPANY_DESC', models.TextField(blank=True, null=True)),
                ('PUB_DATE', models.DateTimeField(auto_now=True, null=True)),
                ('JOBURL', models.URLField(blank=True, max_length=250, null=True)),
                ('JOB_SUMMARY', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emploi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EXPIRYDATE', models.DateTimeField(blank=True, null=True)),
                ('JOBREF', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('LANGUAGE', models.CharField(choices=[('FR', 'FR'), ('EN', 'EN')], default='EN', max_length=2)),
                ('JOBNAME', models.URLField(blank=True, max_length=250, null=True)),
                ('POSITION', models.CharField(blank=True, max_length=150, null=True)),
                ('POSTDATE', models.DateTimeField(blank=True, null=True)),
                ('SALARYMIN', models.CharField(blank=True, max_length=40, null=True)),
                ('SALARYMAX', models.CharField(blank=True, max_length=40, null=True)),
                ('SALARYTYPE', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cityjobs.Description')),
            ],
        ),
    ]
