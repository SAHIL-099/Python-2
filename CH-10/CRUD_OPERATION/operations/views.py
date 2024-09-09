from django.shortcuts import get_object_or_404, render,redirect
from .models import Student
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def student(request):
    student=Student.objects.all()
    if request.method=='POST':
        rollno=request.POST.get('rollno')
        name=request.POST.get('name')
        division=request.POST.get('division')
        
        # Validate input fields
        if  rollno and  name and  division:
                student = Student(roll=rollno, name=name, division=division)
                student.save()  # Save the student to the database
                return redirect('student')
            
    return render(request,'student.html',{'student':student})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('login')
    else:
        form=UserCreationForm()
    
    return render(request,'signup.html',{'form':form})

def login_user(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request, 'Logged in successfully !!')
            return redirect('student')
    else:
        fm=AuthenticationForm
    return render(request,'login.html',{'form':fm})

def logout_user(request):
    logout(request)
    return redirect('login')
@login_required
def update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        rollno = request.POST.get('rollno')
        name = request.POST.get('name')
        division = request.POST.get('division')

        if rollno and name and division:
            try:
                student.roll = rollno
                student.name = name
                student.division = division
                student.save()
                messages.success(request, 'Student updated successfully.')
                return redirect('student')  
            except ValueError:
                messages.error(request, 'Invalid roll number. Please enter a valid integer.')
        else:
            messages.error(request, 'All fields are required.')
    return render(request, 'update.html', {'student': student})



@login_required
def delete(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Student,id=id)
        student.delete()
        messages.success(request,'Student deleted successfully.')
    return redirect('student')



@login_required
def search(request):
    search_query = request.GET.get('roll')  
    if search_query:
        students = Student.objects.filter(roll__icontains=search_query) 
    else:
        students = Student.objects.all()

    return render(request,'search.html', {'students': students})
