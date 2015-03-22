# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ansible', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.RemoveField(
            model_name='credential',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='job',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='jobtemplate',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
    ]
