"""
Views for the lettings application.

Handles HTTP requests and returns rendered templates for letting listings
and detailed letting pages.
"""

from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Render a list view of all lettings.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered template displaying all lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Render a detailed view for a specific letting.

    Args:
        request (HttpRequest): The incoming HTTP request.
        letting_id (int): Unique identifier of the letting.

    Returns:
        HttpResponse: Rendered template displaying letting details.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
