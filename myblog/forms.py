from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
app_name = 'myblog'

class LoginForm(forms.Form):
     username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3', 'id':'password', 'type':'password', 'placeholder':'******************'}))
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'First Name',
                                                             'id': 'username'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'Last Name',
                                                             'id': 'username'}))
    username = forms.CharField(widget=forms.TextInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'username',
                                                             'id': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'email',
                                                             'id': 'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={''
                                                             'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                             'type': 'text',
                                                             'placeholder': 'password',
                                                             'id': 'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={''
                                                                  'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                                  'type': 'text',
                                                                  'placeholder': 'password',
                                                                  'id': 'username'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={''
                                                                  'class': 'bg-gray-200 pl-12 py-2 md:py-4 focus:outline-none w-full',
                                                                  'type': 'text',
                                                                  'placeholder': 'Retype password',
                                                                  'id': 'username'}))
class PostForm(forms.ModelForm):
     class Meta:
          model = Product
          fields = ('name', 'price', 'image')