# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Hosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='created_by',
            field=models.DateTimeField(default=datetime.date(2015, 3, 23), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='updated_by',
            field=models.DateTimeField(default=datetime.date(2015, 3, 23), auto_now=True),
            preserve_default=False,
        ),
    ]
