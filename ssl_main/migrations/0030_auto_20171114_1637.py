# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0029_auto_20171114_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='recognitions',
            name='award_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='recognitions',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.CharField(choices=[('M.Tech', 'M.Tech'), ('Ph.D.', 'Ph.D.'), ('B.Tech', 'B.Tech')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Continuing', 'Continuing')], max_length=200),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='semester',
            field=models.CharField(choices=[('Odd Semester', 'Odd Semester'), ('Even Semester', 'Even Semester')], default='Odd Semester', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('Associate Professor', 'Associate Professor'), ('Professor', 'Professor'), ('Assistant Professor', 'Assistant Professor')], default='', max_length=50),
        ),
    ]
