# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import PlaceDetailView, PlaceListView

urlpatterns = [
    url(r'^$', PlaceListView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9a-z\-]+)/(?P<slug>[\w-]+)/$', PlaceDetailView.as_view(), name="detail"),
]
