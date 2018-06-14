# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-04 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('min', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MinistryObjectives',
            new_name='MinistryObjective',
        ),
        migrations.AlterModelOptions(
            name='ministryobjective',
            options={'permissions': (('read_ministryobjective', 'Can read Objetivo del Ministerio'),), 'verbose_name': 'Objetivo del Ministerio', 'verbose_name_plural': 'Objetivos del Ministerio'},
        ),
    ]
