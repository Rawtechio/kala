# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import UsersDetailView, UsersListView

urlpatterns = [
    url(r'^$', UsersListView.as_view(), name="list"),
    url(r'^(?P<slug>[\w-]+)/$', UsersDetailView.as_view(), name="detail"),
]
