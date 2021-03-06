# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0042_auto_20171118_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='published_year',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('Ph.D.', 'Ph.D.'), ('M.Tech', 'M.Tech')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('Professor', 'Professor'), ('Associate Professor', 'Associate Professor'), ('Assistant Professor', 'Assistant Professor')], default='', max_length=50),
        ),
    ]
