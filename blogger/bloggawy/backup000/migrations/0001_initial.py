# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=1000)),
                ('time', models.TimeField()),
                ('reply_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CommentCurses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_id', models.ForeignKey(to='bloggawy.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Curses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curses_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_text', models.CharField(max_length=2000)),
                ('time', models.TimeField(auto_now_add=True)),
                ('cat_id', models.ForeignKey(to='bloggawy.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_id', models.ForeignKey(to='bloggawy.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('blocked', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_id', models.ForeignKey(to='bloggawy.Category')),
                ('user_id', models.ForeignKey(to='bloggawy.User')),
            ],
        ),
        migrations.AddField(
            model_name='posttag',
            name='tag_id',
            field=models.ForeignKey(to='bloggawy.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(to='bloggawy.User'),
        ),
        migrations.AddField(
            model_name='like',
            name='post_id',
            field=models.ForeignKey(to='bloggawy.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(to='bloggawy.User'),
        ),
        migrations.AddField(
            model_name='commentcurses',
            name='curses_id',
            field=models.ForeignKey(to='bloggawy.Curses'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(to='bloggawy.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(to='bloggawy.User'),
        ),
    ]
