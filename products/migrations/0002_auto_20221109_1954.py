# Generated by Django 2.2 on 2022-11-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_img',
            field=models.ImageField(upload_to='media/product_photos'),
        ),
    ]