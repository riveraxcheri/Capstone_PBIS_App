# Generated by Django 4.2 on 2023-04-24 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='inventory',
            field=models.IntegerField(default=1),
        ),
    ]