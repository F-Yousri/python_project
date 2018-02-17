# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggawy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_photo',
            field=models.ImageField(default=b'static/bloggawy/images/testphoto.jpg', upload_to=b'uploads/'),
        ),
    ]
