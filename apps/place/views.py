# -*- coding: utf-8 -*-

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Place


class PlaceDetailView(DetailView):
    model = Place


class PlaceListView(ListView):
    model = Place
