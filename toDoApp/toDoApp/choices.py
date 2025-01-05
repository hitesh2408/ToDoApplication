"""File to store all the choices for To Do Application."""

from django.db import models

class TaskStatus(models.TextChoices):
    """Class to define all the choices."""

    NOT_STARTED = 'NA'
    IN_PROGRESS = 'IP'
    UNDER_REVIEW = 'UR'
    COMPLETED = 'CP'
    DEFERRED = 'DF'
