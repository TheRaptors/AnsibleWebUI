# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hosts', '0002_auto_20150322_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='wip',
            field=models.IPAddressField(null=True, blank=True),
        ),
    ]
