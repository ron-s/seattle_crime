# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-25 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seattle_crime_app', '0006_auto_20160525_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimemodel',
            name='descriptio',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='crimemodel',
            name='group',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='crimemodel',
            name='offensenum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='crimemodel',
            name='subgroup',
            field=models.CharField(max_length=254),
        ),
    ]