from django.shortcuts import get_object_or_404, render
from .models import Book

def book_list(request):
    books = Book.objects.select_related('category').all()
    context = {
        'books': books
    }
    return render(request, 'catalog/book_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book.objects.select_related('category'), pk=book_id)
    context = {
        'book': book
    }
    return render(request, 'catalog/book_detail.html', context)




