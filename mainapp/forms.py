from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Enter your username',
            'class':'w-full py-3 px-5 rounded-xl !outline-none'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder':'Enter your Email',
            'class':'w-full py-3 px-5 rounded-xl !outline-none'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Enter your password',
            'class':'w-full py-3 px-5 rounded-xl !outline-none'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Re-enter your password',
            'class':'w-full py-3 px-5 rounded-xl !outline-none'}))

class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your user name',
            'class': 'w-full py-4 px-6 rounded-xl !outline-none'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Enter your password',
            'class':'w-full py-5 px-5 rounded-xl !outline-none'}))


class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter user name',
        'class':'w-full py-4 px-6 rounded-xl !outline-none'}))

    password =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class':'w-full py-4 px-6 rounded-xl !outline-none'}))