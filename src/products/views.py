import django
from django.shortcuts import render

# Create your views here.<>

from django.http import HttpResponse

def home(request):
    name = "pharaon"
    number = 55
    mylist = [3, 35, 6, 7, 8]
    context ={
        "nom" : name,
        "numero" : number,
        'maList': mylist
    }
    return render(request, 'index.html', context)

