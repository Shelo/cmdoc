# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


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
    ]
