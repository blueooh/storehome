from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'intro.views.home'),
    url(r'^intro/', include('intro.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
