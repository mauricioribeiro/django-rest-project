# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['id'], 'verbose_name': 'Ticket'},
        ),
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
        ),
    ]