from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.teacher_list, name='list'),
    path('add/', views.add_teacher, name='add'),
]
