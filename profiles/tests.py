"""
Test suite for the profiles application.

Contains unit and integration tests for profile-related views, URLs, and models.
"""

from django.contrib.auth.models import User
from django.urls import reverse, resolve
import pytest

from .models import Profile


# =============================================================================
# UNIT TESTS — test individual components in isolation
# =============================================================================


def test_profiles_url(client):
    """Verify the profiles list URL resolves to the profiles index view."""
    url = reverse('profiles:index')
    assert resolve(url).view_name == 'profiles:index'


def test_profiles_detail_url(client):
    """Test Profiles Detail page resolves to detail view"""
    url = reverse('profiles:profile', args=['testuser'])
    assert resolve(url).view_name == 'profiles:profile'


@pytest.mark.django_db
def test_profile_str():
    """Verify Profile.__str__ returns the associated username."""
    user = User.objects.create_user(username='CrazyBananaMan', password='testpass')
    profile = Profile.objects.create(user=user, favorite_city='Athens')
    assert str(profile) == 'CrazyBananaMan'


# =============================================================================
# INTEGRATION TESTS — test full request/response cycle (URL → view → template)
# =============================================================================


@pytest.mark.django_db
def test_profiles_list_view(client):
    """
    GET /profiles/ returns 200, renders profiles/index.html, and displays heading.

    Verifies URL routing, view execution, and template rendering together.
    """
    response = client.get('/profiles/')
    assert response.status_code == 200
    assert 'profiles/index.html' in [t.name for t in response.templates]
    assert b'Profiles' in response.content


@pytest.mark.django_db
def test_profile_detail_view(client):
    """
    GET /profiles/<username>/ returns 200, renders profile.html, and displays
    the username and favorite city from the created test profile.

    Verifies the full cycle including database lookup and context rendering.
    """
    user = User.objects.create_user(username='CrazyBananaMan', password='testpass')
    Profile.objects.create(user=user, favorite_city='Athens')
    response = client.get(f'/profiles/{user.username}/')
    assert response.status_code == 200
    assert 'profiles/profile.html' in [t.name for t in response.templates]
    assert b'CrazyBananaMan' in response.content
    assert b'Athens' in response.content
