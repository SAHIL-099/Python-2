from django.db import models

# Create your models here.

# students/models.py
from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    division = models.CharField(max_length=5)

    def __str__(self):
        return self.roll_number
