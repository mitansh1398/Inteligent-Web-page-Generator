# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0019_auto_20171111_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='published',
            field=models.CharField(choices=[('Journal', 'journal'), ('Conference', 'conference')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(choices=[('Completed', '1'), ('Continuing', '0')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(default='static/portal/assets/img/find_user.png', upload_to='static/faculty_img/'),
        ),
    ]
