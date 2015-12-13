from django.conf.urls import url
from .views import create_card, get_cards, view_card


urlpatterns = [
    # url(r'^(?P<user_name>[-\w+]+)/$', views.get_cards, name='get_cards')
    url(r'^create_card/$', create_card, name='create'),
    url(r'^get_cards/$', get_cards, name='get'),
    url(r'^view_card/$', view_card, name='view'),
]
