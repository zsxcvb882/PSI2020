# Generated by Django 3.1.3 on 2021-01-29 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_Shop', '0005_remove_orders_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]