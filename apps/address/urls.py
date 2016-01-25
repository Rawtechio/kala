# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from .views import AddressDetailView, AddressListView

urlpatterns = [
    url(r'^$', AddressListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', AddressDetailView.as_view()),
]
