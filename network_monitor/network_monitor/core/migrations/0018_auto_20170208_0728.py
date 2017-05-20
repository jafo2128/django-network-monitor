# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-08 07:28
from __future__ import unicode_literals

import traceback

import requests
from django.conf import settings
from django.db import migrations, models
import network_monitor.helpers.utils


def forwards_func(apps, schema_editor):
    print("Checking mac manufacture of all devices....")
    db_alias = schema_editor.connection.alias
    Device = apps.get_model("core", "Device")
    for device in Device.objects.using(db_alias).all():
        if not device.mac or not device.mac.strip():
            continue

        print("+++ Checking mac manufacture of device {}".format(device.name))
        url = '{}/{}'.format(settings.MACVENDORS_API_URL.rstrip('/'), device.mac)
        try:
            res = requests.get(url, timeout=settings.MACVENDORS_API_TIMEOUT)
        except Exception:
            traceback.print_exc()
            continue
        if res.ok:
            device.mac_manufacture = res.text
            device.save()
            print("*** manufacture for device {} is {}".format(device.name, device.mac_manufacture))
        else:
            print("!!! Not found manufacture for device {}".format(device.name))


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20170129_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='mac_manufacture',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='mac',
            field=network_monitor.helpers.utils.MACAddressField(blank=True, max_length=17, null=True, verbose_name='Mac Address'),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]
