# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_post_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='post_photo',
            field=models.ImageField(upload_to=b'blog'),
        ),
    ]
