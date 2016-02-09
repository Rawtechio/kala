# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):

    list_display = ('name', 'job_title', 'email', 'is_staff', 'is_superuser')

    fieldsets = (
        ("User details", {
            'fields': ('name', 'job_title', 'password',)
        }),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', 'is_staff', 'is_superuser',),
        }),
        ('Contact details', {
            'classes': ('collapse',),
            'fields': ('email', 'phone_number', 'fax_number'),
        }),
        ('Activity', {
            'classes': ('collapse',),
            'fields': ('date_joined', 'last_login',),
        }),
    )

admin.site.register(User, UserAdmin)
