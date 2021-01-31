import crum
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.validators import MinValueValidator
import datetime


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    category_id_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, related_name='product')

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='email')
    adress = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.last_name


class Orders(models.Model):

    def save(self, *args, **kwargs):
        username = crum.get_current_user()
        self.username = username.username
        super(Orders, self).save(*args, **kwargs)

    product = models.ManyToManyField(Product, related_name='order')
    username = models.CharField(max_length=45, blank=True, default=crum.get_current_user(), editable=False)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.datetime.now, editable=False)

    def __str__(self):
        return 'Użytkownik: ' + str(self.username) + ' , ' + 'Data: ' + str(self.date) + ' , ID: ' + str(self.id)


class Payments(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    transaction_number = models.IntegerField()
    date = models.DateField()
