# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 02:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='time',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 25, 2, 16, 15, 352569, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
