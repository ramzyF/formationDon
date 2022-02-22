from asyncio import tasks
from django.shortcuts import render, redirect
from .createForm import *
from .updateForm import *
from datetime import datetime

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
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    context = {
        'task': task,
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

def compareDay(date):
    #tasks = Task.objects.filter(created.strftime("%Y-%m-%d") = )
    pass

def search(request):
    tasks = ''
    dateParam =''
    if request.POST:
        dateParam = request.POST.get('dateInput')#with a string like 2022-02-22
    #in the next line with convert dateParam to a datetime object
        if dateParam:
            dateParam = datetime(int(dateParam[:4]), int(dateParam[5:7]), int(dateParam[8:]))
            tasks = Task.objects.filter(created__year = dateParam.year, 
                                              created__month = dateParam.month,
                                              created__day = dateParam.day)
    #print("ramses=",len(dateParam), 'type=', type(dateParam))
    return render(request,'search.html', context={'tasks':tasks, 'myDate': dateParam})
    
def isCompleted(request, pk):
    #this view will help to mark a task as completed or note
    task = ''
    if request.method == "POST":
        completed = request.POST.get('completed')
        if completed:
            task = Task.objects.filter(id=pk).update(completed = True)
        return redirect('home')
    context = {
        'task': task,
    }
    return redirect('home')