from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class FormBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title','author','pub_date','price']

        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:50%', 'rows':'1'}),
            'author': forms.Select(attrs={'class': 'form-control', 'style': 'width:50%', 'rows':'1', 'choices':'1'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'width:50%', 'rows':'1'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:50%', 'rows':'1'})
        }

    # title = forms.CharField(max_length = 200, required=True)
    # author = forms.ModelChoiceField(queryset = Author.objects.all() , required=True)
    # pub_date = forms.DateField(required=False)
    # price = forms.FloatField()

    # title.widget.attrs.update({'class':'form-control', 'style':'width:50%'})
    # author.widget.attrs.update({'class':'form-control', 'style':'width:50%'})
    # pub_date.widget.attrs.update({'class':'form-control', 'style':'width:50%'})
    # price.widget.attrs.update({'class':'form-control', 'style':'width:50%'})

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('You need to enter not negative price')
        return price




class FormAuthor(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['first_name','second_name', 'email','age']

        widgets = {
            'first_name': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:50%', 'rows':'1'}),
            'second_name': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:50%', 'rows':'1'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width:50%', 'rows':'1'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:50%', 'rows':'1'})
        }
    # first_name = forms.CharField(max_length = 30, required=True)
    # second_name = forms.CharField(max_length = 30, required=True)
    # email = forms.EmailField(max_length=150 )
    # age = forms.IntegerField()

    # first_name.widget.attrs.update({'class':'form-control', 'style':'width:50%'})
    # second_name.widget.attrs.update({'class':'form-control', 'style':'width:50%'})
    # email.widget.attrs.update({'class':'form-control', 'style':'width:50%'})
    # age.widget.attrs.update({'class':'form-control', 'style':'width:50%'})

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise ValidationError('Age cannot be less than 0')
        return age

    # def save(self):
    #     new_author = Author.objects.create(
    #         first_name = self.cleaned_data['first_name'],
    #         second_name = self.cleaned_data['second_name'],
    #         email = self.cleaned_data['email'],
    #         age = self.cleaned_data['age']
    #     )
    #     return new_author
    
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

