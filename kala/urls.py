from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^accounts/', include('authtools.urls')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

    url(r'^user/', include('apps.users.urls', namespace="users")),
    url(r'^address/', include('apps.address.urls', namespace="address")),
    url(r'^organisation/', include('apps.organisation.urls', namespace="organisation")),
    url(r'^place/', include('apps.place.urls', namespace="place")),
    url(r'^admin/', include(admin.site.urls)),
)
