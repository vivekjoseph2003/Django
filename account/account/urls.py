from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', include('signupapi.urls')),
    path('api/login/', include('loginapi.urls')),
]
