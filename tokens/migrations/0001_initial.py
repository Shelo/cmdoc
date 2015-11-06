# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tokens.validators


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=50, serialize=False, primary_key=True, validators=[tokens.validators.validate_token_key])),
                ('value', models.TextField()),
                ('document', models.ForeignKey(to='edit.Document')),
            ],
            options={
                'ordering': ['-document_id', 'key'],
            },
        ),
    ]
