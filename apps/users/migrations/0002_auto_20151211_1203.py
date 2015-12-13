# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(help_text=b'Enter valid email id', max_length=100, null=True, verbose_name=b'Email', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(help_text=b'Enter your first name here', max_length=255, verbose_name=b'First name', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(help_text=b'Enter your last name here', max_length=255, verbose_name=b'Last name', blank=True),
        ),
    ]
