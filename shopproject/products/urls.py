from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.product_create, name='createproduct'),
    path('<int:pk>/', views.product_detail, name='productdetail'),
    path('<int:pk>/update/', views.product_update, name='updateproduct'),
    path('<int:pk>/delete/', views.product_delete, name='deleteproduct'),
    path('<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('send_product_email/<int:pk>/', views.send_product_email, name='send_product_email'),
]
