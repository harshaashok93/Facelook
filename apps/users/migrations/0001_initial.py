# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(help_text=b'Enter you age here', verbose_name=b'Age', blank=True)),
                ('profile_picture', models.FileField(help_text=b'Upload your profile picture here', upload_to=b'/profile picture/', verbose_name=b'Profile Picture', blank=True)),
                ('user', models.OneToOneField(related_name='facelook_user', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
