# Generated by Django 2.2 on 2022-12-07 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_eircode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_line_1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line_2',
            new_name='address_line2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ip',
        ),
    ]