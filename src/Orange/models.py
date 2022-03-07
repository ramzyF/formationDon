from enum import unique
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
  name = models.CharField(max_length=200, null=True)
  age = models.IntegerField(default=18)
  num_agent = models.CharField(max_length=10, default='ORL0000000', unique=True)#l=letter, n=number
  country= models.CharField(max_length=100)
  num_cni = models.CharField(max_length=5, default=00000, unique=True)
  gain = models.IntegerField(default=0)
 

class Client(models.Model):
  name = models.CharField(max_length=200, null=True)
  city= models.CharField(max_length=100)
  num_cni = models.CharField(max_length=5, default=00000, unique=True)
  num_agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.name