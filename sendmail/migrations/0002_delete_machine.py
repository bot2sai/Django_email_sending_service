# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-16 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendmail', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Machine',
        ),
    ]
