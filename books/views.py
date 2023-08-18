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
    #permission_denied_message = 'you have not access to this page'
