from django.urls import path
from products import views

urlpatterns = [
    path('', views.home),
    path('/products/', views.products),
    path('/product/', views.product),
]
