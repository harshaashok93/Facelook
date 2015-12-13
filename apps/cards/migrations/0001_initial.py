# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card_name', models.CharField(help_text=b'Enter your card name here', max_length=255, verbose_name=b'Card name', blank=True)),
                ('card_image', models.ImageField(help_text=b'Upload your card image here', upload_to=b'/card image/', verbose_name=b'Card Image', blank=True)),
                ('card_content', models.CharField(default=b'Card Content', help_text=b'Enter the content of this card here', max_length=1000, verbose_name=b'Card Content', blank=True)),
                ('is_private', models.BooleanField(default=False, help_text=b'Check if it is a private card', verbose_name=b'Is a Private Card')),
                ('user', models.ForeignKey(related_name='card', to='users.UserProfile')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(help_text=b'You can comment on the card here', max_length=1000, verbose_name=b'Comments', blank=True)),
                ('card', models.ForeignKey(related_name='card_comment', to='cards.Card')),
                ('user', models.ForeignKey(related_name='user_comment', to='users.UserProfile')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
