from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
            url(r'^schedule/$', 'intro.views.schedule'),
            url(r'^schedule_events/$', 'intro.views.schedule_events'),
            url(r'^menu/$', 'intro.views.menu'),
            url(r'^favorate/$', 'intro.views.favorate'),
            url(r'^reservation_menu/$', 'intro.views.reservation_menu'),
            url(r'^contact/$', 'intro.views.contact'),
        )
