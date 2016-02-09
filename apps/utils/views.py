# -*- coding: utf-8 -*-
# Created on 5 Feb 2016 at 13:17
from __future__ import unicode_literals, absolute_import

# Django
from django.http import Http404
from django.views.generic.detail import DetailView
from django.conf import settings

# 3rd Party
from hashids import Hashids


class UUIDDetailView(DetailView):

    def get_object(self, queryset=None):
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pkhash = self.kwargs.get("pkhash")
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pkhash is not None:
            hashids = Hashids(salt=settings.SECRET_KEY)
            pk = hashids.decode(pkhash)
            if pk:
                queryset = queryset.filter(pk=pk)

        # Next, try looking up by slug.
        if slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        # If none of those are defined, it's an error.
        if pkhash is None and slug is None:
            raise AttributeError("UUID detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj
