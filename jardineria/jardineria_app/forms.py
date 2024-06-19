from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    pass
    class Meta:
        model=User
        fields=['rut','username','first_name','last_name','email','direccion','password1','password2']