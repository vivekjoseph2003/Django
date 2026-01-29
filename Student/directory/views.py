from django.shortcuts import render

def directory(request):
    my_objects = [
        {'name':'John','grade':'A','result':'Passed'},
        {'name':'Chris','grade':'F','result':'Failed'},
        {'name':'Harry','grade':'B','result':'Passed'}
    ]
    context = {'my_objects': my_objects}
    return render(request, 'a.html', context)