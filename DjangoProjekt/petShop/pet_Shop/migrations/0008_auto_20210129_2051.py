# Generated by Django 3.1.3 on 2021-01-29 19:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pet_Shop', '0007_auto_20210129_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 29, 19, 51, 26, 46678, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_Shop.orders'),
        ),
    ]