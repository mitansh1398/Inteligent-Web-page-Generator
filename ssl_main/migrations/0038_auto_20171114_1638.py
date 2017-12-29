# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0037_auto_20171114_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('ongoing', '0'), ('Completed', '1')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.CharField(choices=[('M.Tech', 'M.Tech'), ('Ph.D.', 'Ph.D.'), ('B.Tech', 'B.Tech')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor')], default='', max_length=50),
        ),
    ]
