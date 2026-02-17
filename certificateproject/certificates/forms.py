from django import forms

class CertificateForm(forms.Form):
    student_name = forms.CharField(max_length=100)
    student_email = forms.EmailField()
    course_name = forms.CharField(max_length=200)
    completion_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
