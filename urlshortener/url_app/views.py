from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm
from django.contrib.auth.decorators import login_required
import random, string
from django.core.paginator import Paginator
import secrets

# List Url and Pagination
@login_required(login_url='/login/')
def url_list(request):
    username = request.user.username
    query = request.GET.get('q', '')
    if query:
        urls = URL.objects.filter(username=username, title__icontains=query) | URL.objects.filter(username=username, url__icontains=query)
    else:
        urls = URL.objects.filter(username=username)

    urls = urls.order_by('-created_time')
    paginator = Paginator(urls, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'url_list.html', {'urls': page_obj, 'query': query})


# Add URL(5 limit)
@login_required(login_url='/login/')
def add_url(request):
    username = request.user.username
    if URL.objects.filter(username=username).count() >= 5:
        return render(request, 'url_limit.html')
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_add = form.save(commit=False)
            url_add.username = username
            url_add.short_url = secrets.token_hex(3)[:6]
            url_add.save()
            return redirect('url_list')
    else:
        form = URLForm()
    return render(request, 'add_url.html', {'form': form})

# Edit
@login_required(login_url='/login/')
def edit_url(request, id):
    username = request.user.username
    url_edit = get_object_or_404(URL, id=id, username=username)
    if request.method == 'POST':
        form = URLForm(request.POST, instance=url_edit)
        if form.is_valid():
            form.save()
            return redirect('url_list')
    else:
        form = URLForm(instance=url_edit)
    return render(request,'edit_url.html',{'form': form})

# Delete
@login_required(login_url='/login/')
def delete_url(request, id):
    username = request.user.username
    url_del = get_object_or_404(URL, id=id, username=username)
    url_del.delete()
    return redirect('url_list') 

# shorturl
def redirect_short_url(request, short_url):
    url_obj = get_object_or_404(URL, short_url=short_url)
    return redirect(url_obj.url)
