"""Handler for all utlities."""


from base.choices import UtilityStatus
from base.models import Utilities


class UtilityHandler:
    """Class for Utility Handler."""

    def __init__(self):
        """Initialize the class."""
        pass

    def get_all_active_utlities(self):
        """Return all utility details."""
        utilities = Utilities.objects.filter(
            #utility_status=UtilityStatus.ACTIVE
        ).values(
            'utility_name', 'utility_description', 'type', 'utility_status', 'utility_path'
        )

        return utilities
