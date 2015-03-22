# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='category',
            field=models.ManyToManyField(to=b'Hosts.Category', null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='cpuinfo',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='device',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='meminfo',
            field=models.IntegerField(max_length=32, null=True, blank=True),
        ),
    ]
