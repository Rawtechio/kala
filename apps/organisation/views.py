# -*- coding: utf-8 -*-

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Organisation


class OrganisationDetailView(DetailView):
    model = Organisation


class OrganisationListView(ListView):
    model = Organisation
