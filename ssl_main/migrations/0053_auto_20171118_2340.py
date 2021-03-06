# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_main', '0052_auto_20171118_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Humanities', 'Humanities'), ('Civil Engineering', 'Civil Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Mathematics', 'Mathematics'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Design', 'Design'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemistry', 'Chemistry'), ('Chemical Engineering', 'Chemical Engineering'), ('Bio-Tech', 'Bio-Tech')], max_length=200),
        ),
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('Completed', '1'), ('ongoing', '0')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(choices=[('Continuing', 'Continuing'), ('Completed', 'Completed')], max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='supervisors',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='thesis_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Humanities', 'Humanities'), ('Civil Engineering', 'Civil Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Mathematics', 'Mathematics'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Design', 'Design'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemistry', 'Chemistry'), ('Chemical Engineering', 'Chemical Engineering'), ('Bio-Tech', 'Bio-Tech')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('Associate Professor', 'Associate Professor'), ('Assistant Professor', 'Assistant Professor'), ('Professor', 'Professor'), ('Head of Department', 'Head of Department')], default='', max_length=50),
        ),
    ]
