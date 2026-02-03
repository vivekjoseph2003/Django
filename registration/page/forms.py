from django import forms
from django.core.validators import validate_email

class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=50,min_length=5)
    email = forms.CharField(max_length=100,min_length=10, validators=[validate_email])
    password = forms.CharField(max_length=20,min_length=8)