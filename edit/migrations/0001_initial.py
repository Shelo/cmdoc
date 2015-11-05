# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cmdocapp.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ['-modify_time'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(related_name='document_owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=512)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(to='edit.Document')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
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
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=50, serialize=False, primary_key=True, validators=[cmdocapp.validators.validate_token_key])),
                ('value', models.TextField()),
                ('document', models.ForeignKey(to='edit.Document')),
            ],
            options={
                'ordering': ['-document_id', 'key'],
            },
        ),
        migrations.AddField(
            model_name='changenotification',
            name='document',
            field=models.ForeignKey(to='edit.Document'),
        ),
        migrations.AddField(
            model_name='changenotification',
            name='modifier',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='changenotification',
            name='section',
            field=models.ForeignKey(to='edit.Section', null=True),
        ),
    ]
