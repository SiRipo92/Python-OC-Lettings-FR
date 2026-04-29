"""
URL configuration for the profiles application.

Defines route patterns and maps them to corresponding view functions.
"""

from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('profiles/', views.index, name='index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]
