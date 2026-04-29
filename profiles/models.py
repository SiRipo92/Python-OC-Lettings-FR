"""
Data models for the profiles application.

Defines user profile extensions associated with Django's built-in
authentication system.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents additional user profile information.

    Extends the built-in Django User model with application-specific
    attributes.

    Attributes:
        user (OneToOneField): Associated User instance.
        favorite_city (CharField): User's preferred city (optional).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the username associated with this profile."""
        return self.user.username
