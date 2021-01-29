from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductList.as_view(), name=views.ProductList.name),
    path('products/<int:pk>', views.ProductDetail.as_view(), name=views.ProductDetail.name),
    path('categories', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),
    path('orders', views.OrderList.as_view(), name=views.OrderList.name),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name=views.OrderDetail.name),
    path('customers', views.CustomerList.as_view(), name=views.CustomerList.name),
    path('customers/<int:pk>', views.CustomerDetail.as_view(), name=views.CustomerDetail.name),
    path('payments', views.PaymentList.as_view(), name=views.PaymentList.name),
    path('payments/<int:pk>', views.PaymentDetail.as_view(), name=views.PaymentDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]