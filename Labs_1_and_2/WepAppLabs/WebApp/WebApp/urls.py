"""
URL configuration for WebApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from my_app1 import views
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetOrders, name='main'),
    path('order/<int:id>/', views.GetOrder, name='order_url'),
    path('order_ok/<int:id>/', views.order_ok, name='order_ok'),
    path(r'products/', views.ProductList.as_view(), name='product-list'),
    path(r'products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path(r'products/<int:pk>/put/', views.put, name='product-put'),
]
