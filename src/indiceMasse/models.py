from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
  name = models.CharField(max_length=200, null=True)
  tel_number = models.CharField(max_length=13, null=True)
  city= models.CharField(max_length=100)

