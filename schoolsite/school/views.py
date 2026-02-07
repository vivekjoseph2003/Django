from django.shortcuts import render

STUDENTS = {
    'Alice': {'Math': 90, 'Science': 85, 'English': 92},
    'Bob': {'Math': 75, 'Science': 80, 'English': 78},
    'Charlie': {'Math': 88, 'Science': 92, 'English': 85},
}

def home(request):
    students = list(STUDENTS.keys())
    return render(request, 'home.html', {'students': students})

def student_result(request, name):
    result = STUDENTS.get(name)
    return render(request, 'student_result.html', {'name': name, 'result': result})
