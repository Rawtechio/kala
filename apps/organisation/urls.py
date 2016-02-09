# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import OrganisationDetailView, OrganisationListView

urlpatterns = [
    url(r'^$', OrganisationListView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9a-z\-]+)/(?P<slug>[\w-]+)/$', OrganisationDetailView.as_view(), name="detail"),
]
