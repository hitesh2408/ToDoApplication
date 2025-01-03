"""Handler for managing all the views."""

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class ToDoTasksView(View):
    """Class based view to manage requests on viewing."""

    def get(self, request):
        """GET method for the class based view."""
        return HttpResponse("Hello there!!")

def index(request):
    """Render index page."""
    return render(request, 'index.html', {})

def about(request):
    """Render about page."""
    return render(request, 'about.html', {})
