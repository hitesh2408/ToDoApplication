"""File for admin settings for the django project."""

from django.contrib import admin
from toDoApp.models import Task

admin.site.register(Task)
