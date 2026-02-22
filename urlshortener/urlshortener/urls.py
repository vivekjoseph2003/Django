from django.contrib import admin
from django.urls import path, include
from login_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name='login'),
    path('accounts/', include('accounts_app.urls')),
    path('login/', include('login_app.urls')),
    path('urls/', include('url_app.urls')),
]