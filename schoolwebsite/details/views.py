from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.core.paginator import Paginator
from django.db.models import Q

def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(name__icontains=query))
    else:
        students = Student.objects.all()
    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'details/list.html', {'page_obj': page_obj, 'query': query})

def student_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        student_class = request.POST['student_class']
        age = request.POST['age']
        Student.objects.create(name=name, student_class=student_class, age=age)
        return redirect('student_list')
    return render(request, 'details/form.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.student_class = request.POST['student_class']
        student.age = request.POST['age']
        student.save()
        return redirect('student_list')
    return render(request, 'details/form.html', {'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'details/confirm_delete.html', {'student': student})
