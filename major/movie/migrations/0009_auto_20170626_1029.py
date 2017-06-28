# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 04:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0008_auto_20170607_1743'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user', 'movie')]),
        ),
    ]
