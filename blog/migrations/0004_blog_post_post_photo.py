# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141202_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='post_photo',
            field=models.ImageField(default=datetime.date(2014, 12, 6), upload_to=b'blog/photos'),
            preserve_default=False,
        ),
    ]
