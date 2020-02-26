from django.shortcuts import render,redirect
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Avg,Max
from django.urls import reverse
from django.views import View

from .forms import *
from .models import *

# Create your views here.

def main_catalog(request):
    books = Book.objects.prefetch_related('author').order_by('title').all()
    avg_price = Book.objects.aggregate(average_prices = Avg('price'))
    avg_age = Author.objects.aggregate(Avg('age'))
    max_price = Book.objects.aggregate(Max_price_of_book = Max('price'))
    
    return render(request, 'catalog/authors.html', {
        'books':books, 
        'avg_price':avg_price, 
        'avg_age':avg_age,
        'max_price':max_price
        })


def book_detail(request,id):
    book = Book.objects.get(id=id)
    return render(request, 'catalog/book_detail.html',{
        'book':book
        })

def author_detail(request,id):
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author = author.id)
    return render(request, 'catalog/author_detail.html',{
    'author':author,
    'books':books
        })

def book_create(request):
    if request.method == 'POST':
        form = FormBook(request.POST)
        if form.is_valid():
            new_book = form.save()
            return redirect(new_book)
    else:
        form = FormBook()

    return render(request, 'catalog/book_create.html', {'form':form} )

def author_create(request):
    if request.method == 'POST':
        form = FormAuthor(request.POST)
        if form.is_valid():
            new_auth = form.save()
            return redirect(new_auth)
    else:
        form = FormAuthor()
    
    return render(request, 'catalog/author_create.html', {'form':form} )

class BookUpdate(View):
    def get(self,request,id):
        upd_book = Book.objects.get(id=id)

        bound_form = FormBook(instance=upd_book)

        return render(request, 'catalog/book_update.html', {'form':bound_form} )
    
    def post(self, request, id):
        
        upd_book = Book.objects.get(id=id)
        bound_form = FormBook(request.POST, instance=upd_book)

        if bound_form.is_valid():
            new_upd_book = bound_form.save()
            return redirect (new_upd_book)
        return render(request, 'catalog/book_update.html', {'form':bound_form} )



class AuthorUpdate(View):
    def get(self,request,id):
        upd_auth = Author.objects.get(id=id)

        bound_form = FormAuthor(instance=upd_auth)

        return render(request, 'catalog/author_update.html', {'form':bound_form} )
    
    def post(self, request, id):
        
        upd_auth = Author.objects.get(id=id)
        bound_form = FormAuthor(request.POST, instance=upd_auth)

        if bound_form.is_valid():
            new_upd_auth = bound_form.save()
            return redirect (new_upd_auth)
        return render(request, 'catalog/author_update.html', {'form':bound_form} )

class AuthorDelete(View):
    def get(self, request, id):
        del_author = Author.objects.get(id=id)
        return render(request, 'catalog/author_delete.html', {'author':del_author})
    def post(self,reques,id):
        del_author = Author.objects.get(id=id)
        del_author.delete()
        return redirect( reverse('bookmarket_url'))

class BookDelete(View):
    def get(self, request, id):
        del_book = Book.objects.get(id=id)
        return render(request, 'catalog/book_delete.html', {'book':del_book})

    def post(self,reques,id):
        del_book = Book.objects.get(id=id)
        del_book.delete()
        return redirect( reverse('bookmarket_url'))

class UserRegister(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'catalog/register.html', {'form':form})
        
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect( reverse('bookmarket_url'))
        return render(request, 'catalog/register.html', {'form':form})





# def book_update(request,id):
#     print(request.POST)
#     if request.method == 'POST':
#         form = FormBook(request.POST)
#         if form.is_valid():
#             upd_book = form.save()
#             return redirect(upd_book)
#     else:
#         upd_book = Book.objects.get(id=id)
#         form = FormBook(upd_book)

#     return render(request, 'test_page1/book_update.html', {'form':form} )