# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_auto_20181122_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='issue_type',
            field=models.CharField(choices=[('Free', 'Free'), ('Upgrade', 'Upgrade')], default='Free', max_length=6),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=6),
        ),
    ]
