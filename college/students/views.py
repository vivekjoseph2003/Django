from django.shortcuts import render, redirect

def home(request):
    return render(request, 'students/home.html')

def student_list(request):
    students = ['Alice', 'Bob', 'Charlie']
    message = "Welcome to the Student Page!"
    return render(request, 'students/student_list.html', {'students': students, 'message': message})

def add_student(request):
    if request.method == 'POST':
        return redirect('students:list')
    return render(request, 'students/add_student.html')
