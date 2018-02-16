# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bloggawy', '0004_auto_20180215_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='comment_content',
        ),
        migrations.RenameField(
            model_name='curse',
            old_name='curse_text',
            new_name='curse_content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='post_content',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='reply_text',
            new_name='reply_content',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat_users',
        ),
        migrations.RemoveField(
            model_name='curse',
            name='curse_comments',
        ),
        migrations.RemoveField(
            model_name='curse',
            name='curse_replies',
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='like_type',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_photo',
            field=models.ImageField(default=b'static/bloggawy/images/testphoto.jpg', upload_to=b'static/bloggawy/images'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default='title', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
