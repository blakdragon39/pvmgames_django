from django.conf.urls import url
from django.contrib.auth import views as auth_views

login_urls = [
    url(r'^signup/$', ),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
