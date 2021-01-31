from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Category, Product, Orders, Employee, Payments
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer, EmployeeSerializer, PaymentsSerializer
from django_filters import DateTimeFilter, NumberFilter, ChoiceFilter, CharFilter, FilterSet, DateFilter
from rest_framework import permissions


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'
    search_fields = ['name']
    filterset_fields = ['name']
    ordering_fields = ['name']
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly, ]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly, ]


class ProductFilter(FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['name', 'from_price', 'to_price']


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-list'
    search_fields = ['name', 'description']
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price']
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly, ]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly, ]


class OrderFilter(FilterSet):
    from_date = DateFilter(field_name='date', lookup_expr='gte')
    to_date = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Orders
        fields = ['product', 'username', 'from_date', 'to_date']


class OrderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    name = 'order-list'
    filterset_class = OrderFilter
    #permission_classes = [permissions.IsAuthenticated]


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    name = 'orders-detail'
    #permission_classes = [permissions.IsAdminUser]


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = "employee-list"
    search_fields = ['first_name', 'last_name']
    filterset_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']
    #permission_classes = [permissions.IsAdminUser]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-detail'
    #permission_classes = [permissions.IsAdminUser]


class PaymentList(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    name = "payments-list"
    #permission_classes = [permissions.IsAdminUser]


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    name = 'payments-detail'
    search_fields = ['transaction_number']
    filterset_fields = ['transaction_number']
    #permission_classes = [permissions.IsAdminUser]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'products': reverse(ProductList.name, request=request),
                         'categories': reverse(CategoryList.name, request=request),
                         'orders': reverse(OrderList.name, request=request),
                         'customers': reverse(EmployeeList.name, request=request),
                         'payments': reverse(PaymentList.name, request=request),
                         })
