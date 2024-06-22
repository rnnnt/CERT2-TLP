from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Project
from .forms import CreateNewProject, EditProjectForm


def home(request):
    return render(request, 'core/home.html')

def exit(request):
    logout(request)
    return redirect('home')

@login_required
def projects(request):
    projects = Project.objects.all()
    return render(request, 'core/projects/projects.html', {'projects': projects})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = CreateNewProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects') 
    else:
        form = CreateNewProject()
    
    return render(request, 'core/projects/create_project.html', {'form': form})


def edicion(request, name):
    project = get_object_or_404(Project, name=name)
    
    if request.method == 'POST':
        form = EditProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')  # Redirigir a la lista de proyectos u otra página después de guardar
    else:
        form = EditProjectForm(instance=project)
    
    return render(request, 'core/projects/edicion.html', {'form': form})


def eliminar(request, name):
    project = get_object_or_404(Project, name=name)
    project.delete()
    return redirect('projects') 

def calendario(request):
    return render(request, 'core/calendario.html')