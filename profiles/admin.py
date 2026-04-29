"""
Admin configuration for the profiles application.

Registers profile-related models for management through
the Django admin interface.
"""

from django.contrib import admin

from .models import Profile

# Register Profile model in Django admin
admin.site.register(Profile)
