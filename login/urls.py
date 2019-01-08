from django.conf.urls import url
from django.contrib.auth import views as auth_views

from login.views import signup

login_urls = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
