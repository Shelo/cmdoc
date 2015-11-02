# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cmdocapp', '0010_section_editing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='editing',
            field=models.ForeignKey(related_name='editing_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
