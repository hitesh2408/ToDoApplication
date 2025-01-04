"""Handler to handle the task related functions."""


from toDoApp.models import Task


class TaskHandler:
    """Class to handle all task related functions."""

    def __init__(self, task_uuid):
        """Initialize the class."""
        self.task_id = task_uuid

    @staticmethod
    def create_task(**kwargs):
        """Create a Task object."""
        pass

    def get_task_by_user(self, user_id):
        """Return all tasks for user."""
        pass
