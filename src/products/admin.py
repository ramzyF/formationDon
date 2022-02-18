from django.contrib import admin
from .models import Products, Student
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'actif','slug')

admin.site.register(Products, AdminProduct)

class AdminProduct(admin.ModelAdmin):
    list_display = ('mat', 'name', 'surname', 'birthD')

admin.site.register(Student, AdminProduct)