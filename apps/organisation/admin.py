# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Organisation

class OrganisationAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner', 'active', 'published')

    fieldsets = (
        ("Basic details", {
            'fields': ('name', 'description', 'logo',)
        }),
        ('Owners', {
            'classes': ('collapse',),
            'fields': ('owner', 'maintained_by',),
        }),
        ('Published and Active state', {
            'classes': ('collapse',),
            'fields': ('active', 'dissolution_date', 'published'),
        }),
    )

admin.site.register(Organisation, OrganisationAdmin)
