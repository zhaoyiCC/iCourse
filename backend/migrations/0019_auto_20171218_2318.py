# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_auto_20171213_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='class_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='college',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='email',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='gender',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='grade',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='identification',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='major',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='phone_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='real_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tongpao_userprofile',
            name='tongpao_username',
            field=models.CharField(max_length=32, null=True),
        ),
    ]