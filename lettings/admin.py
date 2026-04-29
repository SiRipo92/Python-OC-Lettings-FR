"""
Admin configuration for the lettings application.

Registers models to make them manageable through the Django admin interface.
"""

from django.contrib import admin

from .models import Letting
from .models import Address

# Register models to be accessible in Django admin
admin.site.register(Letting)
admin.site.register(Address)
