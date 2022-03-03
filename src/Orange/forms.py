from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


CHOICES =[
  ('', 'Choisissez votre pays'),
  ('cameroun', 'Cameroun'),
  ('gabon', 'Gabon'),
  ('nigeria', 'Nigéria'),
  ('maroc', 'Maroc'),
]


class CreateUserForm(UserCreationForm):
  class meta:
    model = User
    fields = ['username', 'password1', 'password2']
    widgets={
      'username': forms.TextInput(attrs={'placeholder':'Nom d\'utilisateur'}),
      'password1': forms.PasswordInput(attrs={'placeholder':'Mot de passe'}),
      'password2': forms.PasswordInput(attrs={'placeholder':'confirmer le mot de passe'}),
    }
    
class AgentForm(forms.ModelForm):
  class Meta:
    model = Agent
    fields = ('name', 'age', 'country','num_cni')
    widgets = {
      'name': forms.TextInput(attrs={'placeholder':'Votre nom'}),
      'age':forms.NumberInput(attrs={'placeholder':'Age'}),
      'country':forms.Select(choices=CHOICES),
      'numCni':forms.NumberInput(attrs={'placeholder':'Numéro de CNI'}),
    }
    