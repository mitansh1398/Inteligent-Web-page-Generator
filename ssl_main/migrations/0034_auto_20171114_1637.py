# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0033_auto_20171114_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.CharField(choices=[('M.Tech', 'M.Tech'), ('Ph.D.', 'Ph.D.'), ('B.Tech', 'B.Tech')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(choices=[('Continuing', 'Continuing'), ('Completed', 'Completed')], max_length=200),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='semester',
            field=models.CharField(choices=[('Even Semester', 'Even Semester'), ('Odd Semester', 'Odd Semester')], default='Odd Semester', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('Assistant Professor', 'Assistant Professor'), ('Professor', 'Professor'), ('Associate Professor', 'Associate Professor')], default='', max_length=50),
        ),
    ]
