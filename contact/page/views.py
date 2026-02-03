from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
def page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact()
            contact.full_name = form.cleaned_data['full_name']
            contact.email = form.cleaned_data['email']
            contact.phone = form.cleaned_data['phone']
            contact.save()
            return render(request,'form-data.html',{
                'full_name': contact.full_name
            })
    else:
        form = ContactForm()
    return render(request,'index.html',{'form':form})