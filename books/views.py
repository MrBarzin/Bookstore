from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q 
from .models import Book
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin



class BookListView(LoginRequiredMixin,ListView):
    model = Book

    template_name = 'books/book_list.html'

class BookDetailView( LoginRequiredMixin,PermissionRequiredMixin ,DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    permission_required = 'books.special_status'

class SearchResultListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q','')
        return Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
        )