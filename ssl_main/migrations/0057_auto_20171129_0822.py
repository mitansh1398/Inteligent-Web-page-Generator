# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0056_auto_20171129_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Design', 'Design'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Bio-Tech', 'Bio-Tech'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Mathematics', 'Mathematics'), ('Humanities', 'Humanities'), ('Physics', 'Physics')], max_length=200),
        ),
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('Completed', '1'), ('ongoing', '0')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.CharField(choices=[('M.Tech', 'M.Tech'), ('Ph.D.', 'Ph.D.'), ('B.Tech', 'B.Tech')], max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('Design', 'Design'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Bio-Tech', 'Bio-Tech'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Mathematics', 'Mathematics'), ('Humanities', 'Humanities'), ('Physics', 'Physics')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('Professor', 'Professor'), ('Head of Department', 'Head of Department'), ('Associate Professor', 'Associate Professor'), ('Assistant Professor', 'Assistant Professor')], default='', max_length=50),
        ),
    ]
