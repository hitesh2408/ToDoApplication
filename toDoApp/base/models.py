"""File to create base for all models."""

from django.contrib.auth.models import User
from django.db import models

from base.choices import UtilityChoices

class AuditModel:
    """Fields for audit purpose."""
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)


class Utilities:
    """Model for all the Utilities."""
    utility_name = models.CharField(max_length=50)
    utility_description = models.TextField()
    type = models.CharField(
        max_length=5, choices=UtilityChoices, default=UtilityChoices.NOT_APPLICABLE
    )
