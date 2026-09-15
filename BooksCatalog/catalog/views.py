from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404

from catalog.models import Book


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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()



    return render(request, 'catalog/register.html', {'form': form})




