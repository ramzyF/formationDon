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

class CreatePatientForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')
    super(CreatePatientForm, self).__init__(*args, **kwargs)
  name = forms.CharField(label='Nom', widget=forms.TextInput(
    attrs={
      'maxlength': 20,
      'placeholder':'Paul Fotsa',
      
    }
  ))
  tel_number = forms.CharField(label='Numéro Whatsapp', widget=forms.TextInput(
    attrs={
      'maxlength':13,
      'placeholder': 'Exemple: +237677281000',
    }
  ))
  city = forms.CharField(label='Ville', 
              widget=forms.TextInput(
              attrs={
      'maxlength':100,
      'placeholder':'Yaoundé',
    }
  ))
  email = forms.EmailField(label='Email',
                           widget=forms.EmailInput(
                             attrs={
                               'placeholder':'Exemple: blabla@gmail.com',
                             }
                           )
    
  )
  class Meta:
    model = Patient
    fields = ('name', 'email', 'tel_number', 'city', 'password1', 'password2' )
    
  
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if Patient.objects.filter(email = str(email)).exists():
      raise forms.ValidationError("Cette adresse email appartient déjà à un patient") 
  
    return email
  def clean_name(self):
    name = self.cleaned_data.get('name')
    if str(name).isdecimal():
      raise forms.ValidationError("Entrer un nom valide(pas uniquement des chiffres") 
  
    return name
   
  def clean_tel_number(self):
    number = self.cleaned_data.get('tel_number')
    if not '+2376' == str(number)[0:5]:
      raise forms.ValidationError("Le numéro doit commencer par +2376")
    if ' ' in str(number):
      raise forms.ValidationError("Le numéro ne doit pas contenir des espaces")
    else:  
      if len(str(number)[1:]) != 12:
        raise forms.ValidationError("Le numéro doit est composer de 12 nombres exactement")
    return number
    

  
  def clean_city(self):
    city = self.cleaned_data.get('city')
    if str(city).isdecimal():
      raise forms.ValidationError("Entrer une ville valide(pas uniquement des chiffres)") 
  
    return city
  class meta:
    model = User
    fields = ['email', 'password1', 'password2']
    widgets={
      'email': forms.EmailInput(),
      'password1': forms.PasswordInput(),
      'password2': forms.PasswordInput(),
    }
  def clean_password(self):
    password2 = self.cleaned_data.get('password2')
    password2 = self.cleaned_data.get('password2')
    if password2 != password2:
      raise forms.ValidationError("Les mots de passe sont différents") 
  
    return password2
    