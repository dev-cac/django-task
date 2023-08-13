from django.forms import ModelForm
from django import forms

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'project', 'important']

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Titulo del Proyecto", max_length=200)
