# Generated by Django 3.1.3 on 2021-01-29 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_Shop', '0017_auto_20210129_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.utcnow, editable=False),
        ),
    ]