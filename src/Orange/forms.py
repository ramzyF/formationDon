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
  ('yaounde', 'Youndé'),
  ('Limbé', 'Limbé'),
  ('bafia', 'Bafia'),
]

class CreateUserForm(UserCreationForm):
  class meta:
    model = User
    fields = ['username', 'password1', 'password2']
    widgets={
      'username': forms.TextInput(),
      'password1': forms.PasswordInput(),
      'password2': forms.PasswordInput(),
    }
    
    
class AgentForm(forms.ModelForm):
  name = forms.CharField(label='Nom', widget=forms.TextInput())
  age = forms.CharField(label='Age',widget=forms.TextInput(
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
    try:
      age = int(self.cleaned_data.get('age'))
      if int(age) <= 17:
        raise forms.ValidationError('Vous devez avoir au moins 18 ans!')
      return age
    except ValueError:
      forms.ValidationError("votre age n'est pas un chiffre")
    

  def clean_country(self):
    
    country = self.cleaned_data['country']
    if country != 'cameroun':
      raise forms.ValidationError('Le pays doit être le Cameroun!')
    return country
   

  def clean_num_cni(self):
    num_cni = self.cleaned_data.get('num_cni')
    try:
      num_cni = int(self.cleaned_data.get('num_cni'))
      if isinstance(int(num_cni), int):
        if len(self.cleaned_data.get('num_cni')) != 5:
          raise forms.ValidationError('Le numéro de CNI n\'est que composer de 5 chiffres')
        if Agent.objects.filter(num_cni=int(num_cni)):
          raise forms.ValidationError('Ce numéro de CNI appartient déjà à un agent')
        return num_cni
    except ValueError:
      forms.ValidationError("Veuillez entrez 5 chiffres correspondant a votre N° de CNI")
  
    
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
   

  def clean_num_cni(self):
    num_cni = self.cleaned_data.get('num_cni')
    try:
      num_cni = int(self.cleaned_data.get('num_cni'))
      if isinstance(int(num_cni), int):
        if len(self.cleaned_data.get('num_cni')) != 5:
          raise forms.ValidationError('Le numéro de CNI n\'est que composer de 5 chiffres')
        if Client.objects.filter(num_cni=int(num_cni)):
          raise forms.ValidationError('Ce numéro de CNI appartient déjà à un client')
        return num_cni
    except ValueError:
      forms.ValidationError("Veuillez entrez 5 chiffres correspondant a votre N° de CNI")
  