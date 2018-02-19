# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggawy', '0008_auto_20180218_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='reply_comments',
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_comments',
            field=models.ForeignKey(to='bloggawy.Comment', null=True),
        ),
    ]
