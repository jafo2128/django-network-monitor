# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-02 12:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0006_devicefeature_last_round'),
    ]

    operations = [
        migrations.CreateModel(
            name='PingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_time', models.FloatField(null=True, verbose_name='Minimum Time(ms)')),
                ('max_time', models.FloatField(null=True, verbose_name='Maximum Time(ms)')),
                ('avg_time', models.FloatField(null=True, verbose_name='Avgerage Time(ms)')),
                ('mdev_time', models.FloatField(null=True, verbose_name='Median Deviation(ms)')),
                ('packet_loss', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Packet Loss(%)')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Timestamp')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ping_time', to='core.Device')),
            ],
        ),
    ]
