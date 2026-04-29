"""
Views for the profiles application.

Handles HTTP requests and renders templates for profile listings
and individual user profiles.
"""

from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Render a list view of all user profiles.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered template displaying all profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Render a detailed view for a specific user profile.

    Args:
        request (HttpRequest): The incoming HTTP request.
        username (str): Username associated with the profile.

    Returns:
        HttpResponse: Rendered template displaying profile details.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
