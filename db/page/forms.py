from django import forms
class MovieForm(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter movie name'}))
    year= forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Enter release year'}))