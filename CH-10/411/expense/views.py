from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ExpenseForm
from .models import Expense

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add_expense')  # Redirect to add_expense or another page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            user = fm.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('add_expense')  # Redirect to add_expense or another page
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})

def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Assuming Expense model has a user field
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('add_expense')
    else:   
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required
def expense_report(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'report.html', {'expenses': expenses})
