"""
Test suite for the oc_lettings_site project.

Contains unit and integration tests for the project-level index view
and custom error handlers (404, 500).
"""

from django.test import override_settings, RequestFactory
from django.urls import reverse, resolve

from .views import error_500


# =============================================================================
# UNIT TESTS — test individual components in isolation
# =============================================================================
def test_index_url_resolves():
    """Verify the root URL pattern resolves to the index view function."""
    url = reverse('index')
    assert resolve(url).func.__name__ == 'index'

# =============================================================================
# INTEGRATION TESTS — test full request/response cycle (URL → view → template)
# =============================================================================


def test_index(client):
    """
    GET / returns 200, renders index.html, and displays expected page content.

    Verifies URL routing, view execution, and template rendering together.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]
    assert b'Welcome to Holiday Homes' in response.content


@override_settings(DEBUG=False)
def test_error_404_view(client):
    """
    GET on an unknown URL returns 404 and renders the custom 404 template.

    DEBUG must be False for Django to invoke handler404 instead of its debug page.
    """
    response = client.get('/this-url-does-not-exist/')
    assert response.status_code == 404
    assert b'404 Error : Page Not Found' in response.content


def test_error_500_view(client):
    """
    The error_500 view returns 500 and renders the custom 500 template.

    Called directly via RequestFactory since no URL triggers a 500 naturally.
    """
    request = RequestFactory().get('/')
    response = error_500(request)
    assert response.status_code == 500
    assert b'500 : Server Error' in response.content
