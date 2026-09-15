from catalog.views import book_detail, book_list, register
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list, name='book_list'),  
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('register/', register, name='register'),
]