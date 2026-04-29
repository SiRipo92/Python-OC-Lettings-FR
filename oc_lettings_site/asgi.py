"""ASGI configuration for the oc_lettings_site project.

Exposes the ASGI callable as a module-level variable named ``application``.

ASGI (Asynchronous Server Gateway Interface) is the asynchronous
successor to WSGI and is used by ASGI-compatible web servers.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()
