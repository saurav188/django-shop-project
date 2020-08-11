from django.urls import path
from products import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('product/product_id=<pk>', views.product_view),
]
