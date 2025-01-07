"""This file contains the models required for To Do Application."""

import uuid

from django.contrib.auth.models import User
from django.db import models

from base.models import AuditModel

from toDoApp.choices import TaskStatus


class Task(AuditModel):
    """Model for each task in the app."""

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    status = models.CharField(
        max_length=2,
        choices=TaskStatus,
        default=TaskStatus.NOT_STARTED
    )
    user = User()
