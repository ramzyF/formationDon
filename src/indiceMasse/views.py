from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Formation import settings 


# Create your views here.
def home(request):
  context = {}
  
  return render(request, 'index.html', context)
  from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template


def signup(request):
  form = CreatePatientForm()
  if request.method == 'POST':
    form = CreatePatientForm(request.POST)
    if form.is_valid():
      form.save()
      form = CreatePatientForm()
      return redirect('signin')
      
    
  context = {
      'form': form, 
    
  }
  
  return render(request, 'register_page.html',context)

def signin(request): 
  message = ''
  form = CreatePatientForm()
  if request.method == 'POST':
    form = CreatePatientForm(request.POST)
    email = form['email'].value()
    password = form['password1'].value()
    patient = authenticate(request, email=email, password=password)  
    if patient is not None and patient.is_active:
      login(request, patient)
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

def ImcVal(imc):
  if imc < 18.5:
    return 'Maigre'
  elif 18.5 <= imc <= 25:
    return "Normale"
  else:
    return "Obèse"

@login_required
def getImc(request):
  are_valid=True
  message = []
  imc = 0
  if request.method == 'POST':
    poids = str(request.POST['poids'])
    taille = str(request.POST['taille'])
    poids = poids.replace(',', '.')
    taille = taille.replace(',', '.')
    poids = poids.replace(';', '.')
    taille = taille.replace(';', '.')
    if len(poids) == 5:
      if '.' == poids[2] and poids[:2].isdecimal() and poids[3:].isdecimal() and poids != '00,00':
        message.append('Veuillez entrer un poids valide de la forme 03.33, 100.00 par exmple')
        are_valid = False
    elif len(poids) == 6:
      if '.' == taille[3] and taille[:3].isdecimal() and taille[4:].isdecimal() and taille != '000,00':
        message.append('Veuillez entrer un poids valide de la forme 03.33, 100.00 par exmple')
        are_valid = False
    else:
      message.append('Veuillez entrer un poids valide de la forme 03.33, 100.00 par exmple')
      are_valid = False
    if not(len(taille) == 5 and'.' == taille[2] and taille[:2].isdecimal() and taille[3:].isdecimal() and taille != '00,00'):
        message.append('Veuillez entrer une taille valide de la forme 03.33 par exmple')
        are_valid = False
    
    if are_valid:
      imc = float(poids)/(float(taille)**2)*100
      imc = float(str(imc)[:4])
      email_subject = 'MON IMC'
      email_message = 'Bonjour petit' + str(request.user.name)
      from_email = settings.EMAIL_HOST_USER
      to_email = [request.user.email]
      ''' send_mail(email_subject, email_message, from_email, to_email, fail_silently=False) '''
      mail = EmailMessage(email_subject, email_message, from_email, [request.user.email])
      ''' mail.attach_alternative(message, "text/html") '''
      #pdf = render_to_pdf('some_invoice.html')
      #message.attach('invoice.pdf', pdf)
      mail.fail_silently=False
      mail.send()
      
  print('Imc: '+ str(imc) + ' ' + ImcVal(imc) )
  context={
    'messages':message,
    'imc':'Imc: '+ str(imc) + ' ' + ImcVal(imc)  ,

  }
  return render(request, 'calcul.html', context)

 