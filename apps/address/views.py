# -*- coding: utf-8 -*-

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Address


class AddressDetailView(DetailView):
    model = Address


class AddressListView(ListView):
    model = Address
