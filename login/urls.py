from django.conf.urls import url
from django.contrib.auth import views as auth_views

from login.views import signup, home, login_user

login_urls = [
    url(r'^$', home, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),
]
