from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.

class Author(models.Model):
    
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 30)
    second_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length=150, blank=True, null=True)
    age = models.IntegerField(null = True, blank=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        fn = self.first_name + ' ' + self.second_name
        return fn

    def get_absolute_url(self):
        return reverse('author_detail_url',kwargs={'id':self.id})
    
    def get_update_url(self):
        return reverse('author_update_url', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('author_delete_url', kwargs={'id':self.id})        
    
    class Meta:
        ordering = ["second_name"]

class Book(models.Model):

    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200, blank = False)
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'books')
    pub_date = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True,null=True)

    def __str__(self):
        return 'title: {}, author: {}, date: {}, price: {}'.format(
            self.title, self.author, self.pub_date, self.price)

    

    def get_absolute_url(self):
        return reverse('book_detail_url', kwargs={'id':self.id})

    def get_update_url(self):
        return reverse('book_update_url', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('book_delete_url', kwargs={'id':self.id})        


    def full_name_of_book(self):
        fnob = self.author.full_name() + ' ' + self.title
        return fnob

    class Meta:
        ordering = ["title"]





    