from django.shortcuts import render
from .forms import TeacherForm

IMAGE_FILE_TYPES = ['jpg', 'jpeg', 'png']

def add_teacher(request):
    form = TeacherForm()
    message = ""

    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)

        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.profile_photo = request.FILES['profile_photo']

            file_type = teacher.profile_photo.name.split('.')[-1].lower()

            if file_type not in IMAGE_FILE_TYPES:
                message = "Error: Only JPG, JPEG, and PNG files are allowed."
                return render(request, 'teacher_form.html', {'form': form, 'message': message})

            teacher.save()
            message = "Success: Teacher details saved successfully!"
            form = TeacherForm()

    return render(request, 'teacher_form.html', {'form': form, 'message': message})
