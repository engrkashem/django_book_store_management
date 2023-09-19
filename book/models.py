from django.db import models

# Create your models here.


class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror')
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_published = models.DateTimeField(auto_now_add=True)
    last_published = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.book_name} | by {self.author}'
