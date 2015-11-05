# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='document',
        ),
        migrations.RemoveField(
            model_name='section',
            name='editing',
        ),
        migrations.RemoveField(
            model_name='section',
            name='modifier',
        ),
        migrations.RemoveField(
            model_name='section',
            name='owner',
        ),
        migrations.AlterField(
            model_name='changenotification',
            name='section',
            field=models.ForeignKey(to='section.Section', null=True),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
