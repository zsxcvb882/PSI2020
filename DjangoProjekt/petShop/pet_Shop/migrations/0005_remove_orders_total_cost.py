# Generated by Django 3.1.3 on 2021-01-28 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_Shop', '0004_auto_20210128_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='total_cost',
        ),
    ]