
from telnetlib import OUTMRK
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from random import randint, shuffle
from django.contrib.auth.decorators import login_required
from django.db.models import Count


# Create your views here.
def home(request):
  context = {}
  
  return render(request, 'index.html', context)
  

def signup(request):
  form = CreateUserForm()
  patient_form = PatientForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    patient_form = PatientForm(request.POST)
    if form.is_valid() and patient_form.is_valid():
      user = form.save()
      patient = patient_form.save(commit=False)
      patient.user = user
      patient.save()
      form = CreateUserForm()
      patient_form = PatientForm()
      
      return redirect('signin')
      
    
  context = {
      'form': form, 
      'patient_form': patient_form,
      
  }
  
  return render(request, 'register_page.html',context)

def signin(request): 
  message = ''
  form = CreateUserForm()
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)  
    if user is not None and user.is_active:
      login(request, user)
      return redirect('home')
    else:
      message ='Veuillez entrer correctement vos identifiants\ncar soit vous n\'avez pas de compte ou les identifiants sont incorrects !'
  context={
    'form':form,
    'message':message
  }
  return render(request, 'login_page.html', context)

@login_required
def signout(request):
  logout(request)
  return redirect('home')

