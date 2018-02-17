# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bloggawy', '0005_auto_20180215_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_categories',
        ),
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(to='bloggawy.Category', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(to='bloggawy.Post', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
