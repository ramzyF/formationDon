from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .createForm import *
from .updateForm import *


# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('created')
    form = TaskForm()
    
    context = {
        'tasks':  tasks,
        'form':form,
    }
    return render(request, 'index.html', context)

def createTask(request):
    """ form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') """
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            newTask = Task.objects.create(**form.cleaned_data)
            newTask.save()
            form = TaskForm()
        return redirect('home')
    context = {
        'form':form,
    }
    return render(request, 'create_task.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskFormUpdated(request.POST or None, instance = task)
    if request.method == "POST":
        form = TaskFormUpdated(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
            form = TaskFormUpdated()
        return redirect("home")
    context = {
        'form':form,
    }
    return render(request,'update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('home')
    context = {
        'item': item,
    }
    return render(request, 'delete_task.html', context)

def completedTask(request):
    tasks = Task.objects.filter(completed__exact=True).order_by('created')
    context = {
        'tasks':tasks,
    }
    return render(request,'completed_task.html', context)
    
def incompletedTask(request):
    tasks = Task.objects.filter(completed__exact=False).order_by('created')
    context = {
        'tasks':tasks,
    }
    return render(request,'incompleted_task.html', context)
    