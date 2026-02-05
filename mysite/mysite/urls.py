from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.greeting, name='home'),
    path('about-us/', views.aboutUs, name='about-us'),
]
