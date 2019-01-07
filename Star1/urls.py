from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^rss/', include('rss.urls')),
    url(r'^admin/', admin.site.urls),
]