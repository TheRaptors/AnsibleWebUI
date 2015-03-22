# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=128)),
                ('ssh_username', models.CharField(default=b'', max_length=1024, verbose_name=b'SSH username', blank=True)),
                ('ssh_password', models.CharField(default=b'', max_length=1024, verbose_name=b'SSH password', blank=True)),
                ('ssh_key_data', models.TextField(default=b'', verbose_name=b'SSH private key', blank=True)),
                ('ssh_key_unlock', models.CharField(default=b'', max_length=1024, verbose_name=b'SSH key unlock', blank=True)),
                ('sudo_username', models.CharField(default=b'', max_length=1024, blank=True)),
                ('sudo_password', models.CharField(default=b'', max_length=1024, blank=True)),
                ('created_by', models.ForeignKey(related_name=b"{u'class': 'credential', u'app_label': 'ansible'}(class)s_created", on_delete=django.db.models.deletion.SET_NULL, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name=b'credentials', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('inventory', models.CharField(max_length=1024)),
                ('playbook', models.CharField(max_length=1024)),
                ('job_type', models.CharField(max_length=64, choices=[(b'run', b'Run'), (b'check', b'Check')])),
                ('use_sudo', models.NullBooleanField(default=None)),
                ('sudo_user', models.CharField(default=b'', max_length=1024)),
                ('sudo_password', models.CharField(max_length=1024)),
                ('forks', models.PositiveIntegerField(default=0, blank=True)),
                ('limit', models.CharField(default=b'', max_length=1024, blank=True)),
                ('vars_files', models.TextField(default=0, blank=True)),
                ('extra_vars', models.TextField(default=b'', blank=True)),
                ('email', models.TextField(default=b'', blank=True)),
                ('cancel_flag', models.BooleanField(default=False)),
                ('status', models.CharField(default=b'new', max_length=20, editable=False, choices=[(b'new', b'New'), (b'pending', b'Pending'), (b'running', b'Running'), (b'successful', b'Successful'), (b'failed', b'Failed'), (b'error', b'Error'), (b'canceled', b'Canceled')])),
                ('result_stdout', models.TextField(default=b'', editable=False, blank=True)),
                ('result_stderr', models.TextField(default=b'', editable=False, blank=True)),
                ('result_traceback', models.TextField(default=b'', editable=False, blank=True)),
                ('celery_task_id', models.CharField(default=b'', max_length=100, editable=False, blank=True)),
                ('countdown', models.IntegerField(default=0)),
                ('execute_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('created_by', models.ForeignKey(related_name=b"{u'class': 'job', u'app_label': 'ansible'}(class)s_created", on_delete=django.db.models.deletion.SET_NULL, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('credential', models.ForeignKey(related_name=b'jobs', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='Ansible.Credential', null=True)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('playbook', models.CharField(default=b'', max_length=1024)),
                ('inventory', models.CharField(default=b'', max_length=1024)),
                ('hosts', models.CharField(default=b'', max_length=1024)),
                ('user', models.CharField(default=b'', max_length=1024)),
                ('use_sudo', models.NullBooleanField(default=None)),
                ('sudo_user', models.CharField(default=b'', max_length=1024)),
                ('forks', models.PositiveIntegerField(default=0, blank=True)),
                ('limit', models.CharField(default=b'', max_length=1024, blank=True)),
                ('vars_files', models.TextField(default=b'', blank=True)),
                ('extra_vars', models.TextField(default=b'', blank=True)),
                ('email', models.TextField(default=b'', blank=True)),
                ('created_by', models.ForeignKey(related_name=b"{u'class': 'jobtemplate', u'app_label': 'ansible'}(class)s_created", on_delete=django.db.models.deletion.SET_NULL, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('scmurl', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('scmtype', models.CharField(max_length=64)),
                ('scmurl', models.URLField(null=True, blank=True)),
                ('group', models.CharField(max_length=128, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name=b"{u'class': 'project', u'app_label': 'ansible'}(class)s_created", on_delete=django.db.models.deletion.SET_NULL, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'permissions': (('access_proj', 'Access Project'), ('config_proj', 'Config Project'), ('execute_proj', 'Execute Project'), ('manage_proj', 'Manage Project')),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='package',
            name='project',
            field=models.ForeignKey(related_name=b'package', on_delete=django.db.models.deletion.SET_NULL, to='Ansible.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='project',
            field=models.ForeignKey(related_name=b'job_templates', on_delete=django.db.models.deletion.SET_NULL, to='Ansible.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='project',
            field=models.ForeignKey(related_name=b'jobs', on_delete=django.db.models.deletion.SET_NULL, to='Ansible.Project', null=True),
            preserve_default=True,
        ),
    ]
