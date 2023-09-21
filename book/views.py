from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView


# function based view


# def home(request):
#     return render(request, 'home.html')


# class based view
class MyTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context = {'name': 'kashem', 'age': 72}
        context.update(kwargs)  # dictionary update
        return context


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


# def show_books(request):
#     books = BookStoreModel.objects.all()
#     print(books)
#     return render(request, 'show_book.html', {'books': books})

# class based view
class ShowBookView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'books'
    ordering = ['-id']  # reverse order

    # def get_queryset(self) -> QuerySet[Any]:
    #     return BookStoreModel.objects.filter(author='Shakspear')

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context = {'books': BookStoreModel.objects.all().order_by('category')}
    #     return context


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
