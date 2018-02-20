# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bloggawy', '0002_user_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curse_text', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('replay_text', models.CharField(max_length=1000)),
                ('replay_time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='commentcurses',
            name='comment_id',
        ),
        migrations.RemoveField(
            model_name='commentcurses',
            name='curses_id',
        ),
        migrations.RemoveField(
            model_name='posttag',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='posttag',
            name='tag_id',
        ),
        migrations.RemoveField(
            model_name='usercat',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='usercat',
            name='user_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='comment_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='comment_user',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='post_id',
            new_name='like_post',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user_id',
            new_name='like_user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='time',
            new_name='post_time',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='post_user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='user_admin',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='blocked',
            new_name='user_blocked',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='user_password',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply_text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
        migrations.RemoveField(
            model_name='like',
            name='number_likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_users',
            field=models.ManyToManyField(to='bloggawy.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(default=datetime.datetime(2018, 2, 14, 22, 57, 1, 964840, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_categories',
            field=models.ManyToManyField(to='bloggawy.Category'),
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_posts',
            field=models.ManyToManyField(to='bloggawy.Post'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.EmailField(default=datetime.datetime(2018, 2, 14, 22, 57, 43, 619739, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CommentCurses',
        ),
        migrations.DeleteModel(
            name='Curses',
        ),
        migrations.DeleteModel(
            name='PostTag',
        ),
        migrations.DeleteModel(
            name='UserCat',
        ),
        migrations.AddField(
            model_name='replay',
            name='replay_comments',
            field=models.ManyToManyField(to='bloggawy.Comment'),
        ),
        migrations.AddField(
            model_name='replay',
            name='replay_user',
            field=models.ForeignKey(to='bloggawy.User'),
        ),
        migrations.AddField(
            model_name='curse',
            name='curse_comments',
            field=models.ManyToManyField(to='bloggawy.Comment'),
        ),
        migrations.AddField(
            model_name='curse',
            name='curse_replays',
            field=models.ManyToManyField(to='bloggawy.Replay'),
        ),
    ]
