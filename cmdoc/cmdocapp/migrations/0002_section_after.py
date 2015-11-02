# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdocapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='after',
            field=models.ForeignKey(to='cmdocapp.Section', null=True),
        ),
    ]
