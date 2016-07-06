# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-26 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emplois', '0003_auto_20160526_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='LANGUAGE',
        ),
        migrations.AddField(
            model_name='job',
            name='language',
            field=models.CharField(choices=[('FR', 'Francais'), ('EN', 'English')], default='EN', max_length=2),
        ),
    ]