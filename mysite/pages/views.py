from django.shortcuts import render
from .forms import LoginForm

def greeting(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'form-data.html', {
                'data': form.cleaned_data
            })
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

def aboutUs(request):
    return render(request, 'about-us.html')
