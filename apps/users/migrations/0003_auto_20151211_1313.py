# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151211_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='facelook_user', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
