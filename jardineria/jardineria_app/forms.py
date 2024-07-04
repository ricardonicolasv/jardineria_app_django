from django.db import models
from django import forms
from .models import User,Producto
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    pass
    class Meta:
        model=User
        fields=['username','rut','first_name','last_name','email','direccion','password1','password2']

class ProductoForm(forms.ModelForm):
    codigo_producto=forms.CharField(max_length=50,required=True)
    nombre_producto=forms.CharField(max_length=50,required=True)
    class Meta:
        model = Producto
        fields = ['codigo_producto','nombre_producto','cantidad','tipo','precio','imagen']

class UpdProductoForm(forms.ModelForm):
       
    class Meta:
        model = Producto
        fields = ['nombre_producto','cantidad','tipo','precio','imagen']