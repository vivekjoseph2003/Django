from django.shortcuts import render
def details(request):
    if request.GET:
        Username = request.GET.get('user')
        return render(request,'form-data.html',{
            'formData':request.GET,
            'Username': Username
        })
    return render(request,'a.html' )