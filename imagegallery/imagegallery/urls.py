from django.urls import path
from gallery import views
urlpatterns = [
    path('',views.gallerypage,name='gallery'),
    path('contact/',views.contactpage,name='contact'),
]
