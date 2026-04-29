"""
Root URL configuration for the oc_lettings_site project.

Routes incoming HTTP requests to the appropriate application-level
URL configurations or view functions.

Also defines custom error handlers.
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
]

# Custom error handlers
handler404 = views.error_404
handler500 = views.error_500
