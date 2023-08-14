from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),

    path('projects/', views.projects, name="projects"),
    path('tasks/', views.tasks, name="tasks"),
    path('task/<int:id>', views.task, name="task"),
    path('task/<int:id>/complete', views.completeTask, name="complete_task"),
    path('task/<int:id>/delete', views.deleteTask, name="delete_task"),

    path('create/project', views.createProject, name="create_project"),
    path('create/task', views.createTask, name="create_task"),
]
