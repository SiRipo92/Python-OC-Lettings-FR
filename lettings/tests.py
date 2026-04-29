"""
Test suite for the lettings application.

Contains unit and integration tests for lettings-related views, URLs, and models.
"""

from django.urls import reverse, resolve
import pytest

from .models import Address, Letting


# =============================================================================
# UNIT TESTS — test individual components in isolation
# =============================================================================


def test_lettings_url(client):
    """Verify the lettings list URL resolves to the lettings index view."""
    url = reverse('lettings:index')
    assert resolve(url).view_name == 'lettings:index'


def test_lettings_detail_url(client):
    """Verify the letting detail URL resolves to the letting view."""
    url = reverse('lettings:letting', args=[3])
    assert resolve(url).view_name == 'lettings:letting'


@pytest.mark.django_db
def test_address_str():
    """Verify Address.__str__ returns number and street."""
    address = Address.objects.create(
        number=123,
        street='Test Street',
        city='Test City',
        state='CA',
        zip_code=12345,
        country_iso_code='USA'
    )
    assert str(address) == "123 Test Street"


@pytest.mark.django_db
def test_letting_str():
    """Verify Letting.__str__ returns the letting title."""
    address = Address.objects.create(
        number=123,
        street='Test Street',
        city='Test City',
        state='CA',
        zip_code=12345,
        country_iso_code='USA'
    )
    letting = Letting.objects.create(
        title='Test Letting',
        address=address)
    assert str(letting) == "Test Letting"


# =============================================================================
# INTEGRATION TESTS — test full request/response cycle (URL → view → template)
# =============================================================================


@pytest.mark.django_db
def test_lettings_list_view(client):
    """
    GET /lettings/ returns 200, renders lettings/index.html, and displays heading.
    Verifies URL routing, view execution, and template rendering together.
    """
    response = client.get('/lettings/')
    assert response.status_code == 200
    assert 'lettings/index.html' in [t.name for t in response.templates]
    assert b'Lettings' in response.content


@pytest.mark.django_db
def test_lettings_detail_view(client):
    """
    GET /lettings/<id>/ returns 200, renders letting.html, and displays
    the title and address from the created test letting.

    Verifies the full cycle including database lookup and context rendering.
    """
    address = Address.objects.create(
        number=123,
        street='Test Street',
        city='Test City',
        state='CA',
        zip_code=12345,
        country_iso_code='USA'
    )
    letting = Letting.objects.create(
        title='Test Letting',
        address=address
    )
    response = client.get(f'/lettings/{letting.id}/')
    assert response.status_code == 200
    assert 'lettings/letting.html' in [t.name for t in response.templates]
    assert b'Test Letting' in response.content
    assert b'Test Street' in response.content
