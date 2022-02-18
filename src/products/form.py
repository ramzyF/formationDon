from email.policy import default
from timeit import default_timer
from unicodedata import name
from django import forms
from .models import Student
from datetime import date, datetime

class StudentForm(forms.Form):
    mat = forms.CharField(label='Matricule', max_length=12, widget=forms.TextInput(
        attrs={
            'placeholder':'Entrer matricule',
            'maxlength':'10',
            
        }
    ))
    name = forms.CharField(label='Nom', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrer votre nom'
            
        }
    ))
    surname = forms.CharField(label='Prénom', widget=forms.TextInput(
        attrs={
            'placeholder':'Entrer votre prénom'
        }
    ))
    birthD = forms.DateField(label='Date de naissance', widget=forms.DateInput(
        attrs={
            'type':'date'
        }
    ))
    
    #let make take for the values entered in fields
    def clean_mat(self, *args, **kwargs):
       mat = self.cleaned_data.get('mat')
       if not 'CMR' in mat[:3]:
           raise forms.ValidationError('Le matricule doit commencer par "CMR"')
       elif not len(mat) == 12:
           raise forms.ValidationError('Le matricule doit avoir 12 caractères')
       else:
           return mat
   
    
    def clean_birthD(self, *args, **kwargs):
        birthD = self.cleaned_data.get('birthD')
        age = calculateAge(birthD)
        #<br>
        if age < 18:
            raise forms.ValidationError("Vous êtes mineur(-18 ans), ce site n'est \npas fait pour vous. Sinon, \nchanger votre date de naissance.")
        if age > 50:
            raise forms.ValidationError('Vous êtes trop agé pour ce site(+50 ans)')
        else:
            return birthD 
    
def calculateAge(birthDate):
    today = date.today()
    age = today.year-birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age