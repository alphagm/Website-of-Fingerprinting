# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-22 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_remove_webcategories_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcategories',
            name='url',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]