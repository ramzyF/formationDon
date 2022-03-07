from django.contrib import admin
from .models import *

# Register your models here.
class AdminAgent(admin.ModelAdmin):
    list_display = ('num_agent', 'user', 'name', 'gain')

class AdminClient(admin.ModelAdmin):
    list_display = ('num_agent', 'name', 'num_cni','city')
    
admin.site.register(Agent, AdminAgent)
admin.site.register(Client, AdminClient)
