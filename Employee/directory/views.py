from django.shortcuts import render

def directory(request):
    my_objects = [
        {'name':'John','jobtitle':'Analyst','salary':50000,'JobTime':'Full Time'},
        {'name':'Harry','jobtitle':'Data Scientist','salary':10000,'JobTime':'Part Time'},
        {'name':'Chris','jobtitle':'Software Developer','salary':25000,'JobTime':'Full Time'}
    ]
    context = {'my_objects': my_objects}
    return render(request, 'a.html', context)