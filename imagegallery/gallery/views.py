from django.shortcuts import render
def gallerypage(request):
    return render(request,'gallery.html')
def contactpage(request):
    return render(request,'contact.html')