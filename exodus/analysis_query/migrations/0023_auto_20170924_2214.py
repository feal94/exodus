# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_query', '0022_auto_20170924_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrequest',
            name='apk',
            field=models.FileField(upload_to='apks/e233380e-d12a-4462-bcdd-701ad96ee5f5'),
        ),
        migrations.AlterField(
            model_name='analysisrequest',
            name='storage_path',
            field=models.TextField(default='apks/e233380e-d12a-4462-bcdd-701ad96ee5f5'),
        ),
    ]