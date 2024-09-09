from django.shortcuts import render
from .models import Student
# Create your views here.
# Make a student name search form by roll number using Django 


def home(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')  # Get roll number from POST data
        if roll:  # Ensure roll number is provided
            students = Student.objects.filter(roll_number=roll) 
            
        else:
            students = Student.objects.all()

    return render(request,'home.html', {'students': students})  
