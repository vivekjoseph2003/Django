from django.urls import path
from directory import views
urlpatterns = [
  path('',views.directory)
]