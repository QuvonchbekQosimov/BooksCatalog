from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.select_related('category').all()
    context = {
        'books': books
    }
    return render(request, 'catalog/book_list.html', context)




