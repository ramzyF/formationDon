
from telnetlib import OUTMRK
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from random import randint, shuffle
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def formatRank(n):
  if n == 1:
    return "1er"
  else:
    return str(n)+'e'
  
def getRank(user, users):
  i = 0
  while i <= len(users):
    i += 1
    if user.id == users[i-1]:
      return(formatRank(i)) 
    
def sortList(T):
  for i in range(len(T)-1):
    for j in range (i, len(T)):
      if T[i][0] < T[j][0]:
        tmp = T[i]
        T[i] = T[j]
        T[j] = tmp
  return T
  
def sort_dict(querySet):
  tupl = list()
  keys = []
  for i in querySet:
    tupl.append((i['total'],i['num_agent']))
  #trions le la liste de tuples(tri bulle): tupl=[(clientTotal, idAgent)]
  return [val[1] for val in sortList(tupl)]

def ho(request):
  var = Client.objects.values('num_agent',).annotate(total=Count('id'),).order_by()
  print(sort_dict(var))
  context = {
    
  }
  return render(request, 'home.html',context)


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
      form = CreateUserForm()
      agent_form = AgentForm()
      
      return redirect('signin')
      
    
  context = {
      'form': form, 
      'agent_form': agent_form,
      
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
  rank = ''
  gain = 0
  if request.user is not None and request.user.is_active:
    agent = request.user
    clients = Client.objects.filter(num_agent=agent)
    if clients:
      #cherchons le rang
      users = sort_dict(Client.objects.values('num_agent',).annotate(total=Count('id')))
      rank = getRank(agent, users)
      gain = agent.agent.gain
    context = {
      'clients': clients,
      'rank':rank,
      'gain': gain,
      'nbr': 0
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
      #gerons le gain de 100fr
      agent = client.num_agent.agent
      agent.gain += 100
      agent.save()
      #fin
      client.save()
      form = ClientForm()
      return redirect ('home')
  context={
    'form':form,
  }
  return render(request, 'client_registration.html', context)