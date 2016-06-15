from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'YAGPA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^management/', include('management.urls')),
    url(r'^auth/', include('user_auth.urls')),
    url(r'^tournament/', include('tournament.urls')),
]
