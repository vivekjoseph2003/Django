from django.contrib import admin
from django.urls import path, include
from productsapi.views import home

urlpatterns = [
    path('', home), 
    path('admin/', admin.site.urls),
    path('productsapi/', include('productsapi.urls')),
]
