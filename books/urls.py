from django.urls import path
from .views import home, book_list,book_detail, add_book, book_delete, book_update

urlpatterns = [
    path('', home, name='home'),
    path('books/',book_list, name='book_list'),
    path('books/<int:pk>/',book_detail, name='book_detail'),
    path('add-book/', add_book, name='add_book'),
    path('books/<int:pk>/update/', book_update, name='book_update'),
    path('books/<int:pk>/delete/', book_delete, name='book_delete'),
]