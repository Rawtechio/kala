# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import AddressDetailView, AddressListView

urlpatterns = [
    url(r'^$', AddressListView.as_view()),
    url(r'^(?P<pkhash>[0-9a-zA-Z]+)/$', AddressDetailView.as_view()),
]
