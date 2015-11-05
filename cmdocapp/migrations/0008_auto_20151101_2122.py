# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdocapp', '0007_changenotification_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changenotification',
            name='section',
            field=models.ForeignKey(to='cmdocapp.Section', null=True),
        ),
    ]
