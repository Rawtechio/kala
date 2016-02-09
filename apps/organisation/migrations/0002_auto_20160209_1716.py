# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='maintained_by',
            field=models.ManyToManyField(related_name='organisation_maintained_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organisation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisation_owned_by', to=settings.AUTH_USER_MODEL),
        ),
    ]