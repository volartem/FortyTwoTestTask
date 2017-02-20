from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^requests/$', views.middleware_requests, name='middleware'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
