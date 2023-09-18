from django import forms
from book.models import BookStoreModel


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        exclude = ['last_published']