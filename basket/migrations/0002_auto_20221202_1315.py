# Generated by Django 2.2 on 2022-12-02 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basket_items',
            new_name='Basket_item',
        ),
    ]
