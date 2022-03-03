from django.contrib import admin
from .models import *

# Register your models here.
class AdminAgent(admin.ModelAdmin):
    list_display = ('num_gent', 'user', 'name')


admin.site.register(Agent, AdminAgent)
