# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 16:01
from __future__ import unicode_literals

import core.models.utils
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180917_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='createdAt',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name=b'Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='createdBy',
            field=models.EmailField(default=b'system@justto.com', max_length=254, verbose_name=b'Criado por'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='dealValue',
            field=core.models.utils.MoneyField(decimal_places=5, default=0, max_digits=25, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Valor do Acordo'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='dueDate',
            field=models.DateField(blank=True, null=True, verbose_name=b'Data de Devolu\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='lowerRange',
            field=core.models.utils.MoneyField(decimal_places=5, default=0, max_digits=25, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Valor da Al\xc3\xa7ada M\xc3\xadnima'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[(b'OPEN', b'Aberto'), (b'DEALING', b'Em negocia\xc3\xa7\xc3\xa3o'), (b'DEAL_SUCCESS', b'Negociado com sucesso'), (b'DEAL_FAIL', b'N\xc3\xa3o negociado')], default=b'OPEN', max_length=25),
        ),
        migrations.AddField(
            model_name='ticket',
            name='updatedAt',
            field=models.DateField(auto_now=True, verbose_name=b'Atualizado em'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='updatedBy',
            field=models.EmailField(default=b'system@justto.com', max_length=254, verbose_name=b'Atualizado por'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='upperRange',
            field=core.models.utils.MoneyField(decimal_places=5, default=0, max_digits=25, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Valor da Al\xc3\xa7ada M\xc3\xa1xima'),
        ),
    ]
