from rest_framework import serializers
from .models import Category, Product, Orders, Employee, Payments


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product-detail')

    class Meta:
        model = Category
        fields = ['url', 'pk', 'name', 'description', 'product']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category_id_category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Product
        fields = ['url', 'pk', 'name', 'description', 'price', 'stock', 'category_id_category']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(many=True, queryset=Product.objects.all(), view_name='product-detail')

    class Meta:
        model = Orders
        fields = ['url', 'pk', 'product', 'username', 'paid', 'date']
        depth = 1


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'pk', 'first_name', 'last_name', 'email', 'adress', 'phone_number']


class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.SlugRelatedField(queryset=Orders.objects.all(), slug_field='pk')

    class Meta:
        model = Payments
        fields = ['order', 'transaction_number', 'date']
