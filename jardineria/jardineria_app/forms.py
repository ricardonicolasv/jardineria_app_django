from django.db import models
from django import forms
from .models import User,Producto
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from django.core.validators import RegexValidator

class UserForm(UserCreationForm):
    pass
    class Meta:
        model=User
        fields=['username','rut','first_name','last_name','email','direccion','password1','password2']
    rut = forms.CharField(label='RUT', max_length=12, validators=[
        RegexValidator(
            regex=r'^\d{7,8}[-]?[\dkK]$',
            message='El RUT ingresado no es válido',
            code='invalid_rut'
        ),
    ])
    


class ProductoForm(forms.ModelForm):
    codigo_producto=forms.CharField(max_length=50,required=True)
    nombre_producto=forms.CharField(max_length=50,required=True)
    precio= forms.IntegerField(min_value=1, max_value=150000000)

    class Meta:
        model = Producto
        fields = ['codigo_producto','nombre_producto','cantidad','tipo','precio','imagen']

class UpdProductoForm(forms.ModelForm):
       
    class Meta:
        model = Producto
        fields = ['nombre_producto','cantidad','tipo','precio','imagen']