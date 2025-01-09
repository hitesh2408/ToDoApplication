"""Handler for managing all the views."""

from django.shortcuts import render
from django.views import View

from toDoApp.handlers.utility_handler import UtilityHandler


class ToDoTasksView(View):
    """Class based view to manage requests on viewing."""

    def get(self, request):
        """GET method for the class based view."""
        context = {}
        return render(request, 'toDoApp/tasks.html', context)

def index(request):
    """Render index page."""
    utilities = list(UtilityHandler().get_all_active_utlities())
    context = {
        "utlities": utilities,
    }
    return render(request, "index.html", context)

def about(request):
    """Render about page."""
    return render(request, "about.html", {})
