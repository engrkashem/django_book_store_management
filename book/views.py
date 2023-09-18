from django.shortcuts import render
from book.forms import BookStoreForm

# Create your views here.


def home(request):
    return render(request, 'base.html')


def store_book(request):
    books = BookStoreForm(request.POST)
    print(books)
    return render(request, 'store_book.html', {'form': books})
