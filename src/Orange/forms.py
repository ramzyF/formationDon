from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


CHOICES_COUNTRY =[
  ('', ''),
  ('cameroun', 'Cameroun'),
  ('gabon', 'Gabon'),
  ('nigeria', 'Nigéria'),
  ('maroc', 'Maroc'),
]

CHOICES_CITY =[
  ('', ''),
  ('mbouda', 'Mbouda'),
  ('yaounde', 'Yaoundé'),
  ('Limbé', 'Limbé'),
  ('bafia', 'Bafia'),
]

class CreateUserForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super(CreateUserForm, self).__init__(*args, **kwargs)
  class meta:
    model = User
    fields = ['username', 'password1', 'password2']
    widgets={
      'username': forms.TextInput(),
      'password1': forms.PasswordInput(),
      'password2': forms.PasswordInput(),
    }
    
    
class AgentForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super(AgentForm, self).__init__(*args, **kwargs)
        
  name = forms.CharField(label='Nom', widget=forms.TextInput())
  age = forms.CharField(label='Age', widget=forms.TextInput(
    attrs={
      'maxlength':2,
    }
  ))
  country = forms.CharField(label='Pays de résidence', 
              widget=forms.Select(choices=CHOICES_COUNTRY)
            )
  num_cni = forms.CharField(label='Numéro de CNI',widget=forms.TextInput(
    attrs={
      'maxlength':5,
    }
  ))
  class Meta:
    model = Agent
    fields = ('name', 'age', 'country','num_cni')
    
   
  def clean_age(self):
    age = self.cleaned_data.get('age')
    if not str(age).isdecimal():
      raise forms.ValidationError("Veuillez entrez un nombre entier pour l'âge")

    if int(age) <= 17:
      raise forms.ValidationError('Vous devez avoir au moins 18 ans!')
    return age
    

  def clean_country(self):
    
    country = self.cleaned_data['country']
    if country != 'cameroun':
      raise forms.ValidationError('Le pays doit être le Cameroun!')
    return country
   

  def clean_num_cni(self):
    num_cni = self.cleaned_data.get('num_cni')
    if not str(num_cni).isdecimal():
      raise forms.ValidationError("Veuillez entrer 5 chiffres correspondant au N° de CNI")
    if len(self.cleaned_data.get('num_cni')) != 5:
      raise forms.ValidationError('Le numéro de CNI n\'est que composer de 5 chiffres')
    if Agent.objects.filter(num_cni=int(num_cni)):
      raise forms.ValidationError('Ce numéro de CNI appartient déjà à un agent')
    return num_cni
  
    
class ClientForm(forms.ModelForm):
  name = forms.CharField(label='Nom', widget=forms.TextInput())
  num_cni = forms.CharField(label='Numéro de CNI',widget=forms.TextInput(
    attrs={
      'maxlength':5,
    }
  ))
  city = forms.CharField(label='Ville de résidence', widget=forms.Select(choices=CHOICES_CITY))
  class Meta:
    model = Client
    fields = ('name',  'num_cni', 'city')
    help_texts = {
            'num_cni': 'Le numéro de CNI est une suite de 5 chiffres',
        }

  def clean_num_cni(self):
    num_cni = self.cleaned_data.get('num_cni')
    if not str(num_cni).isdecimal():
      raise forms.ValidationError("Veuillez entrer 5 chiffres correspondant au N° de CNI")
    if len(self.cleaned_data.get('num_cni')) != 5:
      raise forms.ValidationError('Le numéro de CNI n\'est que composer de 5 chiffres')
    if Client.objects.filter(num_cni=int(num_cni)):
      raise forms.ValidationError('Ce numéro de CNI appartient déjà à un agent')
    return num_cni
  