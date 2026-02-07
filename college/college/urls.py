from django.contrib import admin
from django.urls import path, include
from students import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_views.home, name='home'),
    path('students/', include('students.urls', namespace='students')),
    path('teachers/', include('teachers.urls', namespace='teachers')),
]
