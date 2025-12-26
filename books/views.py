from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"

class BookCreateView(CreateView):
    model = Book
    template_name = "books/book_form.html"
    fields = '__all__'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    template_name = "books/book_form.html"
    fields = '__all__'
    success_url = reverse_lazy('book_list')

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')
