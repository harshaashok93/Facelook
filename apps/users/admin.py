from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

    list_display = ['username', 'first_name', 'last_name',
                    'email', 'age', 'profile_picture']

    def username(self, instance):
        return instance.user.username

    def first_name(self, instance):
        return instance.user.first_name

    def last_name(self, instance):
        return instance.user.last_name

    def email(self, instance):
        return instance.user.email
    # class Meta:
    #     model = UserProfile
    #     fields = __all__

    # list_display = [
    #     'username', 'first_name', 'last_name',
    #     'email', 'age', 'profile_picture'
    # ]

    # list_filter = ['username']

    # search_fields = ['first_name']

admin.site.register(UserProfile, UserProfileAdmin)
