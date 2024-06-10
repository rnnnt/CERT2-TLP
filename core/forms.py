from django import forms
from .models import Project


class CreateNewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'theme', 'estudiante','profesor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'theme': forms.TextInput(attrs={'class': 'input'}),
            'estudiante': forms.Select(attrs={'class': 'input'}),
            'profesor': forms.Select(attrs={'class': 'input'}),
        }

class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'theme', 'estudiante', 'profesor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'theme': forms.TextInput(attrs={'class': 'input'}),
            'estudiante': forms.Select(attrs={'class': 'input'}),
            'profesor': forms.Select(attrs={'class': 'input'}),
        }

