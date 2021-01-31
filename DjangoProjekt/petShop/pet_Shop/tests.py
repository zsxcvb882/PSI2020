from django import urls
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from . import views
from .models import Employee, Category


# TESTY DLA EMPLOYEES

class EmployeeTests(APITestCase):

    def post_employee(self, first_name, last_name, email, adress, phone_number):
        url = reverse(views.EmployeeList.name)
        data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'adress': adress,
                'phone_number': phone_number}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_employee(self):
        new_first_name = 'Kamil'
        new_last_name = 'Chomej'
        new_email = 'przykladowymail@gmail.com'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'
        response = self.post_employee(new_first_name, new_last_name, new_email, new_adress, new_phone_number)

        assert response.status_code == status.HTTP_201_CREATED
        assert Employee.objects.count() == 1
        assert Employee.objects.get().first_name == new_first_name
        assert Employee.objects.get().last_name == new_last_name
        assert Employee.objects.get().email == new_email
        assert Employee.objects.get().adress == new_adress
        assert Employee.objects.get().phone_number == new_phone_number

    def test_search_employee(self):
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

        self.post_employee(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        self.post_employee(new_first_name1, new_last_name1, new_email1, new_adress1, new_phone_number1)

        search_employee = {'first_name': new_first_name, 'last_name': new_last_name}
        url = '{0}?{1}'.format(reverse(views.EmployeeList.name), urlencode(search_employee))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['first_name'] == new_first_name
        assert response.data['results'][0]['last_name'] == new_last_name

    def test_filter_employee(self):
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

        self.post_employee(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        self.post_employee(new_first_name1, new_last_name1, new_email1, new_adress1, new_phone_number1)

        filter_employee = {'first_name': new_first_name, 'last_name': new_last_name}
        url = '{0}?{1}'.format(reverse(views.EmployeeList.name), urlencode(filter_employee))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['first_name'] == new_first_name
        assert response.data['results'][0]['last_name'] == new_last_name

    def test_order_employee(self):
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

        self.post_employee(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        self.post_employee(new_first_name1, new_last_name1, new_email1, new_adress1, new_phone_number1)

        ordering_employee = {'first_name': new_first_name, 'last_name': new_last_name}
        url = '{0}?{1}'.format(reverse(views.EmployeeList.name), urlencode(ordering_employee))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['first_name'] == new_first_name
        assert response.data['results'][0]['last_name'] == new_last_name

    def test_delete_employee(self):
        new_first_name = 'Rafał'
        new_last_name = 'Kokoskdosksokd'
        new_email = 'ooiojo@gmail.com'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'

        response = self.post_employee(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        url = urls.reverse(views.EmployeeDetail.name, None, {response.data['pk']})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_update_employee(self):
        new_first_name = 'Alex'
        new_last_name = 'Ostrowski'
        new_email = 'ususuus@gmail.com'
        new_adress = 'nowy Adres'
        new_phone_number = '123456789'

        response = self.post_employee(new_first_name, new_last_name, new_email, new_adress, new_phone_number)
        url = urls.reverse(views.EmployeeDetail.name, None, {response.data['pk']})
        update_first_name = 'Mateusz'
        data = {'first_name': update_first_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['first_name'] == update_first_name


# TESTY DLA CATEGORIES

class CategoriesTests(APITestCase):

    def post_categories(self, name, description):
        url = reverse(views.CategoryList.name)
        data = {'name': name, 'description': description}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_customers(self):
        new_name = 'Pandy'
        new_description = 'Egzotyczne zwierzęta'
        response = self.post_categories(new_name, new_description)

        assert response.status_code == status.HTTP_201_CREATED
        assert Category.objects.count() == 1
        assert Category.objects.get().name == new_name
        assert Category.objects.get().description == new_description

    def test_search_customers(self):
        new_name = 'Pandy'
        new_description = 'Egzotyczne zwierzęta'

        new_name1 = 'Pandy1'
        new_description1 = 'Egzotyczne zwierzęta1'

        self.post_categories(new_name, new_description)
        self.post_categories(new_name1, new_description1)

        search_categories = {'name': new_name, 'description': new_description}
        url = '{0}?{1}'.format(reverse(views.CategoryList.name), urlencode(search_categories))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_name
        assert response.data['results'][0]['description'] == new_description

    def test_delete_categories(self):
        new_name = 'Pandy'
        new_description = 'Egzotyczne zwierzęta'

        response = self.post_categories(new_name, new_description)
        url = urls.reverse(views.CategoryDetail.name, None, {response.data['pk']})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_update_customers(self):
        new_name = 'Pandy'
        new_description = 'Egzotyczne zwierzęta'

        response = self.post_categories(new_name, new_description)
        url = urls.reverse(views.CategoryDetail.name, None, {response.data['pk']})
        update_name = 'Niedzwiedzie'
        data = {'name': update_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == update_name

    def test_filter_categories(self):
        new_name = 'Pandy'
        new_description = 'Egzotyczne zwierzęta'

        new_name1 = 'Pandy'
        new_description1 = 'Egzotyczne zwierzęta'

        self.post_categories(new_name, new_description)
        self.post_categories(new_name1, new_description1)

        filter_categories = {'name': new_name, 'description': new_description}
        url = '{0}?{1}'.format(reverse(views.CategoryList.name), urlencode(filter_categories))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2
        assert response.data['results'][0]['name'] == new_name
        assert response.data['results'][0]['description'] == new_description
