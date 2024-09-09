from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    type=models.CharField(max_length=2, choices=[('nv','novel'),('sf','Sciencefiction'),('ft','Fantasy')])
    
    def __str__(self):
        return self.name