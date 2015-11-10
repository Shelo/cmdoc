# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_section_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='serial',
            field=models.IntegerField(default=0),
        ),
    ]
