from django.shortcuts import render,redirect
from django.db.models import Q  # Import Q for complex queries
from .models import Book

def home(request):
    if request.method == 'POST':
        books=Book.objects.all()
        query = request.POST.get('query')  
        if query:  
            # Use Q objects to filter by name or author
            books = Book.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))
        
        else:
            books=Book.objects.all()
            

    # Render the template with the books context
    return render(request, 'home.html', {'books': books})
