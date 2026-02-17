from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup_api'),
    path('login', views.login, name='login_api'),
    path('add_note', views.add_note, name='add_note_api'),
    path('list_notes', views.list_notes, name='list_notes_api'),
]
