"""File to have base for all choices."""

from django.db import models

class UtilityChoices(models.TextChoices):
    """Class for Utility choices."""

    NOT_APPLICABLE = "NA"
    DAILY_USE = "DU"
    MATHEMATICAL = "MT"
    FILE_HANDLING = "FH"
