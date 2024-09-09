from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=70)
    division=models.CharField(max_length=70)
    