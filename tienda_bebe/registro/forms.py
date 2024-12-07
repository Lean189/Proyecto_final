from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Usuario

class RegistroFormulario(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']


class LoginFormulario(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')
    password= forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class ProfileForm(UserChangeForm):
    avatar = forms.ImageField(required=False) 

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'avatar']