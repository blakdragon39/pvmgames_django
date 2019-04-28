"""
https://docs.djangoproject.com/en/1.11/topics/http/urls/

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from bingo import views
from games.urls import game_urls
from login.urls import login_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns.extend(login_urls)
urlpatterns.extend(game_urls)

handler404 = views.error_404
