from cProfile import label
from django import forms
from django.forms import ModelForm
from .models import *


""" class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__' """
        
class TaskFormUpdated(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 
            'completed',
            ]
        labels = {
            'title':'Titre de la tâche',
            'completed': 'Terminée'
        }
    