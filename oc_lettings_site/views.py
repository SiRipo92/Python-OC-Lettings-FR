"""
Views for the oc_lettings_site project.

Defines project-level views, including the homepage and
custom error pages.
"""
from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the homepage.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered homepage template.
    """
    return render(request, 'index.html')


def error_404(request, exception):
    """
    Render the custom 404 error page.

    Args:
        request (HttpRequest): The incoming HTTP request.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: Rendered 404 error template.
    """
    logger.warning('404 error: %s', request.path)
    return render(request, '404.html', status=404)


def error_500(request):
    """
    Render the custom 500 error page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered 500 error template.
    """
    logger.error('500 error at: %s', request.path)
    return render(request, '500.html', status=500)
