from django.shortcuts import render, redirect

def teacher_list(request):
    teachers = ['Mr. Smith', 'Mrs. Johnson', 'Ms. Lee']
    message = "Welcome to the Teacher Page!"
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers, 'message': message})

def add_teacher(request):
    if request.method == 'POST':
        return redirect('teachers:list')
    return render(request, 'teachers/add_teacher.html')
