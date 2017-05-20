# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-11 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_event_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertnotification',
            name='severity',
            field=models.SmallIntegerField(choices=[(5, 'Critical'), (4, 'Error'), (3, 'Warning'), (2, 'Info'), (1, 'Debug'), (0, 'Clear')], default=2, verbose_name='Severity'),
        ),
        migrations.AlterField(
            model_name='useralertrule',
            name='rules',
            field=jsonfield.fields.JSONField(default=dict, verbose_name='Rules'),
        ),
    ]
