# -*- coding: utf-8 -*-

from apps.utils.views import UUIDDetailView
from django.views.generic.list import ListView

from .models import Address


class AddressDetailView(UUIDDetailView):
    model = Address


class AddressListView(ListView):
    model = Address
