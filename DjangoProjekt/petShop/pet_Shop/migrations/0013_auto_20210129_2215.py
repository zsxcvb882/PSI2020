# Generated by Django 3.1.3 on 2021-01-29 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_Shop', '0012_auto_20210129_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime.now, editable=False),
        ),
    ]
