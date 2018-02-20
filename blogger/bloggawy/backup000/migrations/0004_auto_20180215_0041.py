# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggawy', '0003_auto_20180214_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply_text', models.CharField(max_length=1000)),
                ('reply_time', models.TimeField(auto_now_add=True)),
                ('reply_comments', models.ManyToManyField(to='bloggawy.Comment')),
                ('reply_user', models.ForeignKey(to='bloggawy.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='replay',
            name='replay_comments',
        ),
        migrations.RemoveField(
            model_name='replay',
            name='replay_user',
        ),
        migrations.RemoveField(
            model_name='curse',
            name='curse_replays',
        ),
        migrations.DeleteModel(
            name='Replay',
        ),
        migrations.AddField(
            model_name='curse',
            name='curse_replies',
            field=models.ManyToManyField(to='bloggawy.Reply'),
        ),
    ]
