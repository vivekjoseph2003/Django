from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        return render(request, 'about.html')
    else:
        return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')
