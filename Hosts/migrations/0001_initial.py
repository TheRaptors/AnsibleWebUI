# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catname', models.CharField(unique=True, max_length=128)),
                ('port', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gname', models.CharField(unique=True, max_length=128)),
                ('description', models.TextField(max_length=1024, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddr', models.IPAddressField(unique=True)),
                ('hostname', models.CharField(max_length=128, null=True, blank=True)),
                ('user', models.CharField(default=b'root', max_length=128)),
                ('password', models.CharField(max_length=256)),
                ('is_sudo', models.BooleanField(default=False)),
                ('cpuinfo', models.CharField(max_length=256, null=True, blank=True)),
                ('meminfo', models.IntegerField(max_length=32, null=True, blank=True)),
                ('device', models.CharField(max_length=256, null=True, blank=True)),
                ('wip', models.IPAddressField(null=True, blank=True)),
                ('category', models.ManyToManyField(to='Hosts.Category', null=True)),
                ('group', models.ForeignKey(to='Hosts.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
