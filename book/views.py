from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel

# Create your views here.


def home(request):
    return render(request, 'base.html')


def store_book(request):
    if request.method == 'POST':
        books = BookStoreForm(request.POST)
        if books.is_valid():
            # print(books.cleaned_data)
            books.save(commit=True)
            return redirect('show_books')
    else:
        books = BookStoreForm()
    return render(request, 'store_book.html', {'form': books})


def show_books(request):
    books = BookStoreModel.objects.all()
    print(books)
    return render(request, 'show_book.html', {'books': books})


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    return render(request, 'store_book.html', {'form': form})


def delete_book(request, id):
    book = BookStoreModel.objects.get(pk=id).delete()
    return redirect('show_books')
