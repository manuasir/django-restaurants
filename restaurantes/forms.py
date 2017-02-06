from django import forms
from myapp.models import Dreamreal

class RestaurantForm(forms.Form):
   nombre = forms.CharField(max_length = 100)
   direccion = forms.CharField(widget = forms.PasswordInput())
