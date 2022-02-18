from http.client import LENGTH_REQUIRED
from unicodedata import name
from django.db import models

"""Chaque fois que je modifie ma table ou ma class du model
voici les deux commandes a inserer
1- python3 manage.py  makemigrations
2- python3 manage.py migrate"""

#la classe meta travaille sur les données de la grande class products

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    actif = models.BooleanField(default=True)
    slug = models.SlugField(null= True, blank=True)
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")
    
    def __str__(self):
        return self.name


class Student(models.Model):
    mat = models.CharField(primary_key= True, max_length= 10)
    name = models.CharField(max_length= 100)
    surname = models.CharField(max_length= 100)
    birthD = models.DateField()
    
    def __str__(self):
        return self.mat