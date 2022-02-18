from hashlib import new
import django
from django.shortcuts import render

from products.models import Student
from .form import StudentForm
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

def studentCreate(request, *args, **kwargs):
    form = StudentForm()
    message =''
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = Student.objects.create(**form.cleaned_data)
            new.save()
            form = StudentForm()
            message = 'Student registration was a success'
            
    return render(request, 'index.html', {'form': form, 'message': message})

