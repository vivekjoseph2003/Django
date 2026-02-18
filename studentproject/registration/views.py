from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

IMAGE_FILE_TYPES = ['jpg', 'jpeg', 'png']

def register_student(request):
    form = StudentForm()
    message = ""

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            student = form.save(commit=False)
            student.id_card = request.FILES['id_card']

            file_type = student.id_card.name.split('.')[-1]
            file_type = file_type.lower()

            if file_type not in IMAGE_FILE_TYPES:
                message = "Error: File type not supported. Only jpg, jpeg, png allowed."
                return render(request, 'register.html', {'form': form, 'message': message})

            student.save()
            message = "Success: Student registered successfully!"
            return render(request, 'register.html', {'form': StudentForm(), 'message': message})

    return render(request, 'register.html', {'form': form, 'message': message})
