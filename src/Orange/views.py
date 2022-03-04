from atexit import register
from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from random import randint, shuffle
from django.contrib.auth.decorators import login_required
""" 
def checkData(userForm, agentForm):
    messages={}
    #check the age:
    if int(agentForm['age'].value()) <= 17:
        messages[1] = 'Votre devez avoir au moins 18 ans!'
    if len(agentForm['age'].value()) < 1 or len(agentForm['age'].value()) >= 3:
        messages[2] = 'Veuillez entrer un âge valide!'
    if (agentForm['country'].value()) != 'cameroun':
        messages[3]= 'Le pays doit être le Cameroun!'
    if int(agentForm['num_cni'].value()) <= 0:
        messages[4] = 'Le N° de CNI doit être strictement positif!'
    if len(agentForm['num_cni'].value()) != 5:
        messages[5] = 'Le N° de CNI doit contenir 5 chiffres!'
    if User.objects.filter(username=userForm['username']):
        messages[6] = 'Ce nom d\'utilisateur est deja pris'
    ''' else:
        if userForm['password2'].value() != userForm['password1'].value():
            messages[7] = 'Les mots de passe sont differents' '''
    return messages """
def genererMainPart():
    i = 7
    tmp =''
    while i:
        tmp += str(randint(0, 9))
        i -= 1
        
    tmp = list(tmp)
    shuffle(tmp)
    tmp = ''.join(tmp)
    return str(chr(randint(ord('A'), ord('Z')))) + tmp


def genererIdAgent():
    listeAgent = Agent.objects.all().values('num_agent')
    idAgent =''
    print(listeAgent)
    while idAgent == '':
        idAgent += genererMainPart()
        if idAgent in listeAgent:
            continue

        
    return 'OR' + idAgent

# Create your views here.
def home(request):
  context = {}
  if request.user is not None and request.user.is_active:
    agent = request.user
    clients = Client.objects.filter(num_agent=agent)
    context = {
      'clients': clients
    }
  return render(request, 'index.html', context)
  

def signup(request):
  form = CreateUserForm()
  agent_form = AgentForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    agent_form = AgentForm(request.POST)
    if form.is_valid() and agent_form.is_valid():
      user = form.save()
      agent = agent_form.save(commit=False)
      agent.user = user
      agent.num_agent = genererIdAgent()
      agent.save()
      return redirect('signin')
      
    
  context = {
      'form': form, 
      'agent_form': agent_form,
      'messages': messages
  }
  
  return render(request, 'register_page.html',context)

def signin(request):
  message = ''
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)  
    if user is not None and user.is_active:
      login(request, user)
      return redirect('home')
    else:
      message ='Veuillez entrer correctement vos identifiants\ncar soit vous n\'avez pas de compte ou les identifiants sont incorrects !'
  
  return render(request, 'login_page.html', {'message':message})

@login_required
def signout(request):
  logout(request)
  return redirect('home')


def dashboard(request):
  context = {}
  if request.user is not None and request.user.is_active:
    agent = request.user
    clients = Client.objects.filter(num_agent=agent)
    context = {
      'clients': clients
    }
  return render(request, 'dashboard.html', context)

@login_required
def registerClient(request, pk=None):
  form = ClientForm()
  if request.method == "POST":
    form = ClientForm(request.POST)
    if form.is_valid():
      client = form.save(commit=False)
      client.num_agent = User.objects.get(pk=request.user.id)
      client.save()
      form = ClientForm()
      return redirect ('home')
  context={
    'form':form,
  }
  return render(request, 'client_registration.html', context)