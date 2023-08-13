from django.contrib import admin
from django import forms

from .models import Project, Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    empty_value_display = 'N/A'

# Register your models here.
admin.site.register(Project)
admin.site.register(Task, TaskAdmin)
