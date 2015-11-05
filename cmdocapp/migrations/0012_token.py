# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cmdocapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdocapp', '0011_auto_20151102_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=50, serialize=False, primary_key=True, validators=[cmdocapp.models.validate_token_key])),
                ('value', models.TextField()),
                ('document', models.ForeignKey(to='cmdocapp.Document')),
            ],
            options={
                'ordering': ['-document_id', 'key'],
            },
        ),
    ]
