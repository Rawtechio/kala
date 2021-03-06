# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('street_address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('county', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('postal_code', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
