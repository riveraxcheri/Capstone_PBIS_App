# Generated by Django 4.2 on 2023-04-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='total_cost',
            field=models.IntegerField(default=0),
        ),
    ]