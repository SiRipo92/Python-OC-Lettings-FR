"""
Data models for the lettings application.

Defines the core database schema for rental listings and their associated
addresses using Django ORM models.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address associated with a letting.

    Attributes:
        number (PositiveIntegerField): Street number (max 4 digits).
        street (CharField): Street name.
        city (CharField): City name.
        state (CharField): State or region code (2 characters).
        zip_code (PositiveIntegerField): Postal code (max 5 digits).
        country_iso_code (CharField): ISO country code (3 characters).
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Return a human-readable representation of the address."""
        return f'{self.number} {self.street}'

    class Meta:
        """Metadata options for the Address model."""
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """
    Represents a rental property listing.

    Attributes:
        title (CharField): Title or name of the letting.
        address (OneToOneField): Associated Address instance.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the title of the letting."""
        return self.title
