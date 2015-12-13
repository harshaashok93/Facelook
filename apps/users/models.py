from django.db import models
from django.contrib.auth.models import User


# Change the model name to something else
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='facelook_user',
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )

    # firstname = models.CharField(
    #     max_length=255,
    #     blank=False,
    #     verbose_name='First name',
    #     help_text='Enter your first name here'
    # )

    # lastname = models.CharField(
    #     max_length=255,
    #     blank=True,
    #     verbose_name='Last name',
    #     help_text='Enter your last name here'
    # )

    # email = models.EmailField(
    #     blank=False,
    #     null=True,
    #     max_length=100,
    #     verbose_name='Email',
    #     help_text='Enter valid email id'
    # )

    age = models.IntegerField(
        blank=True,
        verbose_name='Age',
        help_text='Enter you age here'
    )

    profile_picture = models.FileField(
        upload_to='/profile picture/',
        blank=True,
        verbose_name='Profile Picture',
        help_text='Upload your profile picture here'
    )

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __unicode__(self):
        return self.user.username
