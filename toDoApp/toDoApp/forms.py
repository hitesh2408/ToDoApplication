"""Handles all the forms for to do app."""

from django import forms

from toDoApp.choices import TaskStatus

class TaskForm(forms.Form):
    """Class for Task Model."""
    name = forms.CharField(max_length=100)
    description = forms.Textarea()
    status = forms.ChoiceField(choices=TaskStatus)
