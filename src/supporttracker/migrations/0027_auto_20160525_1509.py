# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporttracker', '0026_auto_20160524_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='method',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='date_mailed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_to_send',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='referral',
            name='date_referred',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='remind_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thankyou',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voicemail',
            name='date_left',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]