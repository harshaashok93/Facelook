from django.contrib import admin
from .models import Card, Comment


# class CardAdmin(admin.modelAdmin):

admin.site.register(Card)
admin.site.register(Comment)
