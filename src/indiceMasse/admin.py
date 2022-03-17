from django.contrib import admin
from .models import *

# Register your models here.
class AdminPatient(admin.ModelAdmin):
    list_display = ('name','email', 'tel_number', 'city')


    
admin.site.register(Patient, AdminPatient)
 
