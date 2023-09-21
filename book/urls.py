from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    # path('', views.TemplateView.as_view(template_name='home.html')),
    path('<int:roll>/', views.MyTemplateView.as_view()),
    path('store_new_book/', views.store_book, name='store_book'),
    # path('show_all_book/', views.show_books, name='show_books'),
    path('show_all_book/', views.ShowBookView.as_view(), name='show_books'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),

]
