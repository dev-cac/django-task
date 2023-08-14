from django.forms import ModelForm
from django import forms

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'project', 'important']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'important': forms.CheckboxInput(
                attrs={'class': 'form-check-input text-center'}
            )
        }

class CreateNewProject(forms.Form):
    name = forms.CharField(
        label="Name Project",
        max_length=200,
        widget= forms.TextInput(attrs={'class': 'form-control'})
    )
