# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edit', '0002_auto_20151105_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('position', models.IntegerField(default=0)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=256, blank=True)),
                ('document', models.ForeignKey(to='edit.Document')),
                ('editing', models.ForeignKey(related_name='editing_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modifier', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name='section_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-document_id', 'position'],
            },
        ),
    ]
