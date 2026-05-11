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
def test_profiles_list_view_context_contains_all_profiles(client):
    """
    The list view's context exposes every Profile under 'profiles_list'.
    Confirms data is actually passed to the template, not just that the
    page renders an empty shell.
    """
    user1 = User.objects.create_user(username='alice', password='x')
    user2 = User.objects.create_user(username='bob', password='x')
    Profile.objects.create(user=user1, favorite_city='Paris')
    Profile.objects.create(user=user2, favorite_city='Rome')
    response = client.get('/profiles/')
    assert 'profiles_list' in response.context
    assert response.context['profiles_list'].count() == 2
    assert b'alice' in response.content
    assert b'bob' in response.content


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


@pytest.mark.django_db
def test_profile_detail_view_context_object(client):
    """
    Detail view exposes 'profile' in the template context and it points to
    the correct Profile instance. Guards against the lookup silently returning
    the wrong record after future refactors.
    """
    user = User.objects.create_user(username='zara', password='x')
    profile = Profile.objects.create(user=user, favorite_city='Lima')
    response = client.get(f'/profiles/{user.username}/')
    assert response.context['profile'] == profile
    assert response.context['profile'].favorite_city == 'Lima'


@pytest.mark.django_db
def test_profile_detail_view_unknown_username_raises(client):
    """
    Requesting a profile for a username that doesn't exist exercises the
    Profile.DoesNotExist branch of the view (lines 45-47). The view re-raises
    after logging, which Django translates into a 500 response in test mode.
    """
    with pytest.raises(Profile.DoesNotExist):
        client.get('/profiles/no-such-user/')
