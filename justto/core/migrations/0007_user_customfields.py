# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-24 21:12
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180919_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='customFields',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True, verbose_name=b'Campos Customiz\xc3\xa1veis'),
        ),
    ]
