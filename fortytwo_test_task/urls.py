from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.hello import views
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
