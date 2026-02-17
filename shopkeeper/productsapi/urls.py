from django.urls import path
from . import views

urlpatterns = [
    path('add_product', views.add_product, name='add_product'),
    path('list_products', views.list_products, name='list_products'),
    path('<int:pk>/update_product', views.update_product, name='update_product'),
    path('<int:pk>/delete_product', views.delete_product, name='delete_product'),
]
