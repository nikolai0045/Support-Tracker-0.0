# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporttracker', '0023_auto_20160509_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='answered',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='left_message',
            field=models.BooleanField(default=False),
        ),
    ]