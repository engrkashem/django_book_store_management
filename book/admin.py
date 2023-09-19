from django.contrib import admin
from book.models import BookStoreModel

# Register your models here.


class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'category',
                    'first_published', 'last_published')


admin.site.register(BookStoreModel, BookStoreModelAdmin)
