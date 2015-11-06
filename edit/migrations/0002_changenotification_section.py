# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
        ('edit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='changenotification',
            name='section',
            field=models.ForeignKey(to='section.Section', null=True),
        ),
    ]
