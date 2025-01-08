"""File for admin settings for the django project."""

from django.contrib import admin

from base.models import Utilities

from toDoApp.models import Task

admin.site.register(Task)
admin.site.register(Utilities)
