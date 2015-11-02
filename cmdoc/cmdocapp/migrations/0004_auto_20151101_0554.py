# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdocapp', '0003_auto_20151101_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='after_who',
        ),
        migrations.AddField(
            model_name='section',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
