from django import forms
class ContactForm(forms.Form):
    full_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Full Name'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))