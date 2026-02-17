from django.contrib import admin
from django.urls import path, include
from notesapi.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('notesapi/', include('notesapi.urls')),
]
