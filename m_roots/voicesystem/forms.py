from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from voicesystem.models import Account


class RegistrationForm(UserCreationForm):
    email        = forms.EmailField(max_length=60, help_text='Enter a valid email address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail'}))
    first_name   = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name    = forms.CharField(max_length=60,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    password1    = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2    = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


    class Meta:
        model = MyAccounts
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')