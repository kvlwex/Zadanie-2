from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_books(request):
    return redirect('book_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('authors/', include('authors.urls')),
    path('', redirect_to_books),  # главная страница теперь ведёт на /books/
]


