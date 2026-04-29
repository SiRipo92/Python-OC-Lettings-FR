"""
WSGI configuration for the oc_lettings_site project.

Exposes the WSGI callable as a module-level variable named ``application``.

WSGI (Web Server Gateway Interface) defines the standard interface
between web servers and Python web applications.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
