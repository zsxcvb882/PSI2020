from django.contrib import admin
from .models import Category, Product, Customers, Orders, Payments

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Orders)
