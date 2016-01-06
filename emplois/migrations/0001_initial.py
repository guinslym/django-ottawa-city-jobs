# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 04:15
from __future__ import unicode_literals

import autoslug.fields
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
                ('salarytype', models.CharField(blank=True, max_length=250, null=True)),
                ('knowledge', models.TextField(blank=True, null=True)),
                ('languagecert', models.TextField(blank=True, null=True)),
                ('educationandexp', models.TextField(blank=True, null=True)),
                ('company_desc', models.TextField(blank=True, null=True)),
                ('salarymin', models.CharField(blank=True, max_length=40, null=True)),
                ('pub_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joburl', models.URLField(blank=True, max_length=250, null=True)),
                ('expirydate', models.DateField(auto_now=True, null=True)),
                ('salarymax', models.CharField(blank=True, max_length=40, null=True)),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('language', models.CharField(choices=[('FR', 'Francais'), ('EN', 'English')], default='EN', max_length=2)),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
                ('jobref', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('job_summary', models.TextField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now=True, null=True)),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=['position', 'pub_date__month'])),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='jobs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplois.Job'),
        ),
    ]
