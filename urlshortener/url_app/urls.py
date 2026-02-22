from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_list, name='url_list'),
    path('add/', views.add_url, name='add_url'),
    path('edit/<int:id>/', views.edit_url, name='edit_url'),
    path('delete/<int:id>/', views.delete_url, name='delete_url'),
]