# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdocapp', '0004_auto_20151101_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(to='cmdocapp.Document')),
            ],
            options={
                'ordering': ['-modify_time'],
            },
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['-document_id', 'position']},
        ),
        migrations.AddField(
            model_name='changenotification',
            name='section',
            field=models.ForeignKey(to='cmdocapp.Section'),
        ),
    ]
