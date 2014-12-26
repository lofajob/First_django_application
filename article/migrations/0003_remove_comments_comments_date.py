# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_comments_comments_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_date',
        ),
    ]
