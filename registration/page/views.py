from django.shortcuts import render
from .forms import RegistrationForm
def page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return render(request,'form-data.html',{
                 'full_name': form['full_name'].value
             })
    else:
        form = RegistrationForm()
    return render(request,'index.html',{'form':form})