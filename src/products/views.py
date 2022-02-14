import django
from django.shortcuts import render

# Create your views here.<>

from django.http import HttpResponse

from products.models import Products


def allProduct(request):
    product = Products.objects.all().order_by('price')
    return render(request, 'index.html', {'products': product})

def productLessOneD(request):
    product = Products.objects.filter(price__lt = 1)
    return render(request, 'home1.html', {'products': product})

def productBetOne_Onethousand(request):
    product = Products.objects.filter(price__gte = 1, price__lte = 1000)
    return render(request, 'home2.html', {'products': product})

def productMoreOneThousand(request):
    product = Products.objects.filter(price__gt = 1000)
    return render(request, 'home3.html', {'products': product})