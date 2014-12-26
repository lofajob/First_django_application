# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from random import randrange


def comment_auth_attach(article, schema_editor):
    comments = article.get_model("article", "comments").objects.all()
    for comment in comments:
        rand_id = randrange(1, 6)
        #comment.comment_author = orm['auth.User'].objects.get(id=rand_id)
        #comment.comment_author_id = article.get_model["auth", "User"].objects.get(id=rand_id)
        comment.comment_author_id = rand_id
        comment.save()


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comments_comment_author'),
    ]

    operations = [
        migrations.RunPython(comment_auth_attach),
    ]
