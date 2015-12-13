from django.conf.urls import url
from .views import home, register, login, account


urlpatterns = [
    # url(r'^(?P<user_name>[-\w+]+)/$', views.get_profile, name='get_profile'),
    url(r'^$', home, name='home'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^account/$', account, name='account'),
]
