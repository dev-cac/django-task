from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .forms import TaskForm, CreateNewProject
from .models import Project, Task


# Create your views here.
def index(req):
    return render(req, "home.html")


def signup(req):
    error = ""

    if req.method == "POST":
        if req.POST["password1"] == req.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=req.POST["username"], password=req.POST["password1"]
                )

                user.save()
                login(req, user)
                return redirect("tasks")
            except IntegrityError:
                error = 'El Usuario ya existe'
        else:
            error = 'Las contraseñas no coinciden'

    return render(req, "signup.html", {"form": UserCreationForm, "error": error})

def signout(req):
    logout(req)
    return redirect('index')

def signin(req):
    error = ""

    if req.method == 'POST':
        user = authenticate(
            req,
            username=req.POST['username'],
            password=req.POST['password']
        )

        if user is None:
            error = 'Usuario o Contraseña incorrectos'
        else:
            login(req, user)
            return redirect('tasks')

    return render(req, 'signin.html', {
        'form': AuthenticationForm,
        'error': error
    })

def projects(req):
    projects = list(Project.objects.values())
    return render(req, "projects/projects.html", {"projects": projects})


def tasks(req):
    tasks = list(Task.objects.values())
    return render(req, "tasks/tasks.html", {"tasks": tasks})


def task(req, id):
    task = get_object_or_404(Task, id=id)
    return render(req, "tasks/task.html", {"task": task})


def createTask(req):
    error = ''

    if req.method == "POST":
        try:
            form = TaskForm(req.POST)
            newTask = form.save(commit=False)
            newTask.user = req.user

            newTask.save()
            return redirect("tasks")
        except ValueError:
            error = 'Valide la información proporcionada'

    return render(req, "tasks/create_task.html", {
        "form": TaskForm,
        "error": error
    })


def createProject(req):
    if req.method == "POST":
        Project.objects.create(
            name=req.POST["name"],
        )

        return redirect("projects")
    else:
        return render(req, "projects/create_project.html", {"form": CreateNewProject()})
