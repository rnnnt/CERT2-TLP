from django.urls import path
from .views import home, exit, projects, create_project, eliminar, edicion, calendario

urlpatterns = [
    path('', home, name='home'),
    path('logout/', exit, name='exit'),
    path('projects/', projects, name="projects"),
    path('create_project/', create_project, name="create_project"),
    path('edicion/<name>', edicion, name="edicion"),
    path('projects/eliminar/<name>/', eliminar, name='eliminar'),
    path('calendario/', calendario, name="calendario"),    
]