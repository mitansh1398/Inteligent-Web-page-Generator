# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0039_auto_20171114_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mail_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='random_string',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('ongoing', '0'), ('Completed', '1')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('Ph.D.', 'Ph.D.')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Continuing', 'Continuing')], max_length=200),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='semester',
            field=models.CharField(choices=[('Even Semester', 'Even Semester'), ('Odd Semester', 'Odd Semester')], default='Odd Semester', max_length=200),
        ),
    ]
