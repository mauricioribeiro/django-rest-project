# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS hstore"),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processNumber', models.CharField(blank=True, max_length=25, null=True, verbose_name=b'N\xc3\xbamero do Processo')),
            ],
        ),
    ]
