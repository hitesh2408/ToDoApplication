"""File to create base for all models."""

import uuid

from django.contrib.auth.models import User
from django.db import models

from base.choices import UtilityChoices

class AuditModel(models.Model):
    """Fields for audit purpose."""
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_created_user')
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_modified')

    class Meta:
        """Meta parameters for the model."""
        abstract = True


class Utilities(AuditModel):
    """Model for all the Utilities."""
    uuid = models.UUIDField(primary_key=True, default=uuid.UUID, editable=False)
    utility_name = models.CharField(max_length=50)
    utility_description = models.TextField()
    type = models.CharField(
        max_length=2,
        choices=UtilityChoices,
        default=UtilityChoices.NOT_APPLICABLE
    )
