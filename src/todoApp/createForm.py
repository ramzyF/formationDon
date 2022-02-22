from django import forms
from django.forms import ModelForm
from .models import *


""" class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__' """
class TaskForm(forms.Form):
    title = forms.CharField(label="Titre de la tâche")
    #completed = forms.BooleanField()
    #created = forms.DateTimeField()