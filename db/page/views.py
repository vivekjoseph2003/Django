from django.shortcuts import render
from .forms import MovieForm
from .models import Movie
def page(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = Movie()
            movie.name = form.cleaned_data['name']
            movie.year = form.cleaned_data['year']
            movie.save()
            return render(request,'form-data.html',{
                'name': movie.name,
                'year': movie.year
            })
    else:
        form = MovieForm()
    return render(request,'index.html',{'form':form})