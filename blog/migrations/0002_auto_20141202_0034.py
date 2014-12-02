# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post_Content',
        ),
        migrations.AddField(
            model_name='title',
            name='post_content_text',
            field=models.TextField(default=datetime.date(2014, 12, 2)),
            preserve_default=False,
        ),
    ]
