from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def login_user(request):
    error = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('url_list')
        else:
            error = "Invalid username or password"
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error': error})

@login_required(login_url='/login/')
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')