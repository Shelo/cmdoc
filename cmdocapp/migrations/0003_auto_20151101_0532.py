# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdocapp', '0002_section_after'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='after',
            new_name='after_who',
        ),
    ]
