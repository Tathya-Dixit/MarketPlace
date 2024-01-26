from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

tailclasses = 'rounded-lg bg-gray-200 pl-3'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class' : tailclasses
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your Password',
        'class' : tailclasses
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class' : tailclasses
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your Email',
        'class' : tailclasses
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your Password',
        'class' : tailclasses
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
        'class' : tailclasses
    }))

