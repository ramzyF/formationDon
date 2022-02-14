import django
from django.shortcuts import render

# Create your views here.<>

from django.http import HttpResponse

def home(request):
    mylist = [3, 35, 6, 7, 8]
    context ={
        'maList': mylist
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request,'contact.html')

def filtre(request):
    mylist = [3, 35, 6, 7, 8]
    context ={
        'liste': mylist
    }
    return render(request, 'index1.html', context)