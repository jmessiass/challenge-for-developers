# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 04:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170928_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repositorie',
            old_name='repositorie_language',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='repositorie',
            old_name='repositorie_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='repositorie',
            old_name='repositorie_tag',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='repositorie',
            old_name='repositorie_url',
            new_name='url',
        ),
    ]
