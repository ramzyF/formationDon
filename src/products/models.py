from django.db import models

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
    
    
        
"""Chaque fois que je modifie ma table ou ma class du model
voici les deux commandes a inserer
1- python manage.py  makemigrations
2- python manage.py migrate"""

#la classe meta travaille sur les données de la grande class products