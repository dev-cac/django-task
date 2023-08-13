from django.shortcuts import get_object_or_404, render, redirect

from .forms import CreateNewTask, CreateNewProject
from .models import Project, Task

# Create your views here.
def index(req):
    title = 'Welcome to Djangooo!!'
    return render(req, 'index.html', {
        'title': title
    })

def projects(req):
    projects = list(Project.objects.values())
    return render(req, 'projects/projects.html', {
        'projects': projects
    })

def tasks(req):
    tasks = list(Task.objects.values())
    return render(req, 'tasks/tasks.html', {
        'tasks': tasks
    })

def task(req, id):
    task = get_object_or_404(Task, id=id)
    return render(req, 'tasks/task.html', {
        'task': task
    })

def createTask(req):
    if req.method == 'POST': 
        Task.objects.create(
            name=req.POST['title'],
            description=req.POST['description'],
            project_id=5
        )

        return redirect('tasks')
    else: 
        return render(req, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })

def createProject(req):
    if req.method == 'POST':
        Project.objects.create(
            name=req.POST['name'],
        )

        return redirect('projects')
    else: 
        return render(req, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
