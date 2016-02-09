# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Place

class PlaceAdmin(admin.ModelAdmin):

    list_display = ('name', 'parent_organisation', 'owner', 'email', 'published')

    fieldsets = (
        ("Basic details", {
            'fields': ('name', 'owner', 'parent_organisation', 'logo', 'description', 'duns',)
        }),
        ('Contact details', {
            'classes': ('collapse',),
            'fields': ('address', 'email', 'phone_number', 'fax_number',),
        }),
        ('Mapping', {
            'classes': ('collapse',),
            'fields': ('latitude', 'longitude',),
        }),
        ('Published and Active state', {
            'classes': ('collapse',),
            'fields': ('active', 'dissolution_date', 'published'),
        }),
    )

admin.site.register(Place, PlaceAdmin)
