from django.contrib import admin
from django.urls import path, include
from .view import *

urlpatterns = [
    path('bookmarket', main_catalog, name = 'bookmarket_url'),
    path('bookmarket/books/<int:id>', book_detail, name = 'book_detail_url'),
    path('bookmarket/authors/<int:id>', author_detail, name='author_detail_url'),
    path('bookmarket/books/create', book_create, name='book_create_url'),
    path('bookmarket/authors/create', author_create, name='author_create_url'),
    path('bookmarket/books/<int:id>/update', BookUpdate.as_view(), name='book_update_url'),
    path('bookmarket/authors/<int:id>/update', AuthorUpdate.as_view(), name='author_update_url'),
    path('bookmarket/books/<int:id>/delete', BookDelete.as_view(), name='book_delete_url'),
    path('bookmarket/authors/<int:id>/delete', AuthorDelete.as_view(), name='author_delete_url'),
    path('bookmarket/register', UserRegister.as_view(), name = 'user_register_url'),
    path('', include('django.contrib.auth.urls'), name = 'user_login_url'),
]