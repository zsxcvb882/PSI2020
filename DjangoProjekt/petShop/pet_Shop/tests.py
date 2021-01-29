from django import urls
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from . import views
from .models import Customers, Category


class CustomersTests(APITestCase):

    def post_customers(self, first_name, last_name, email, adress, phone_number):
        url = reverse(views.CustomerList.name)
        data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'adress': adress,
                'phone_number': phone_number}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_customers(self):
        new_first_name = 'Kamil'
        new_last_name = 'Chomej'
        new_email = 'przykladowymail@gmail.com'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'
        response = self.post_customers(new_first_name, new_last_name, new_email, new_adress, new_phone_number)

        assert response.status_code == status.HTTP_201_CREATED
        assert Customers.objects.count() == 1
        assert Customers.objects.get().first_name == new_first_name
        assert Customers.objects.get().last_name == new_last_name
        assert Customers.objects.get().email == new_email
        assert Customers.objects.get().adress == new_adress
        assert Customers.objects.get().phone_number == new_phone_number

    def test_search_customers(self):
        new_first_name = 'Bartosz'
        new_last_name = 'Nowak'
        new_email = 'nowak@outlook.com'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'

        new_first_name1 = 'Piotr'
        new_last_name1 = 'Wiśniewski'
        new_email1 = 'asindaoisnd@gmail.com'
        new_adress1 = 'nowy Adres1'
        new_phone_number1 = '123456789'

        self.post_customers(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        self.post_customers(new_first_name1, new_last_name1, new_email1, new_adress1, new_phone_number1)

        search_customers = {'first_name': new_first_name, 'last_name': new_last_name}
        url = '{0}?{1}'.format(reverse(views.CustomerList.name), urlencode(search_customers))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['first_name'] == new_first_name
        assert response.data['results'][0]['last_name'] == new_last_name

    def test_filter_customers(self):
        new_first_name = 'Antoni'
        new_last_name = 'Antonii'
        new_email = 'antoni@wp.pl'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'

        new_first_name1 = 'Paweł'
        new_last_name1 = 'Przykladowenazwisko'
        new_email1 = 'ojishdib@gmail.com'
        new_adress1 = 'nowy Adres1'
        new_phone_number1 = '123456789'

        self.post_customers(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        self.post_customers(new_first_name1, new_last_name1, new_email1, new_adress1, new_phone_number1)

        filter_customers = {'first_name': new_first_name, 'last_name': new_last_name}
        url = '{0}?{1}'.format(reverse(views.CustomerList.name), urlencode(filter_customers))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['first_name'] == new_first_name
        assert response.data['results'][0]['last_name'] == new_last_name

    def test_order_customers(self):
        new_first_name = 'Alan'
        new_last_name = 'Alanik'
        new_email = 'asodoasj@wp.pl'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'

        new_first_name1 = 'Popop'
        new_last_name1 = 'asasasas'
        new_email1 = 'asdasdad@onet.pl'
        new_adress1 = 'nowy Adres1'
        new_phone_number1 = '123456789'

        self.post_customers(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        self.post_customers(new_first_name1, new_last_name1, new_email1, new_adress1, new_phone_number1)

        ordering_customers = {'first_name': new_first_name, 'last_name': new_last_name}
        url = '{0}?{1}'.format(reverse(views.CustomerList.name), urlencode(ordering_customers))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['first_name'] == new_first_name
        assert response.data['results'][0]['last_name'] == new_last_name

    def test_delete_customers(self):
        new_first_name = 'Rafał'
        new_last_name = 'Kokoskdosksokd'
        new_email = 'ooiojo@gmail.com'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'

        response = self.post_customers(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        url = urls.reverse(views.CustomerDetail.name, None, {response.data['pk']})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_update_customers(self):
        new_first_name = 'Alex'
        new_last_name = 'Ostrowski'
        new_email = 'ususuus@gmail.com'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'

        response = self.post_customers(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        url = urls.reverse(views.CustomerDetail.name, None, {response.data['pk']})
        update_first_name = 'Mateusz'
        data = {'first_name': update_first_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['first_name'] == update_first_name

