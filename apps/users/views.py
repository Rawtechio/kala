# -*- coding: utf-8 -*-

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import User


class UsersDetailView(DetailView):
    model = User


class UsersListView(ListView):
    model = User
