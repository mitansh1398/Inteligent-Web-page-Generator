# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0007_auto_20171111_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('ongoing', '0'), ('Completed', '1')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(default='/static/portal/assets/img/find_user.png', upload_to=''),
        ),
    ]
