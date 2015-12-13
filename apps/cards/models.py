from django.db import models
from apps.users.models import UserProfile


class Card(models.Model):
    user = models.ForeignKey(
        UserProfile,
        related_name='card',
        on_delete=models.CASCADE
    )

    card_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Card name',
        help_text='Enter your card name here'
    )

    card_image = models.ImageField(
        upload_to='/card image/',
        blank=True,
        verbose_name='Card Image',
        help_text='Upload your card image here'
    )

    card_content = models.CharField(
        max_length=1000,
        blank=True,
        default="Card Content",
        verbose_name='Card Content',
        help_text='Enter the content of this card here'
    )

    is_private = models.BooleanField(
        default=False,
        verbose_name='Is a Private Card',
        help_text='Check if it is a private card'
    )

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __unicode__(self):
        return self.card_name


class Comment(models.Model):
    user = models.ForeignKey(
        UserProfile,
        related_name='user_comment',
        on_delete=models.CASCADE
    )

    card = models.ForeignKey(
        Card,
        related_name='card_comment',
        on_delete=models.CASCADE
    )

    comment = models.CharField(
        max_length=1000,
        verbose_name='Comments',
        help_text='You can comment on the card here',
        blank=True,
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __unicode__(self):
        return self.comment
