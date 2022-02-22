from django.contrib import admin
from .models import *


class AdminTask(admin.ModelAdmin):
    list_display = ('id','title', 'completed', 'created')
# Register your models here.
admin.site.register(Task, AdminTask)