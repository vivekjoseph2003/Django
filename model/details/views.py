from django.shortcuts import render
from .forms import BookModelForm
from .models import Book
def details(request):
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            mod = Book.objects.all()
            return render(request,'form-data.html',{
                'message': 'Book Info Stored',
                'books': mod
            })
    else:
        form = BookModelForm()
    return render(request,'index.html',{'form':form})