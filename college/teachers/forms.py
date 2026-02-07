from django import forms

class TeacherForm(forms.Form):
    name = forms.CharField(label='Teacher Name', max_length=100)
