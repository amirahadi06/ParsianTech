# Generated by Django 3.2.6 on 2021-09-25 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_alter_service_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='contact_customer',
            new_name='customer_service',
        ),
        migrations.RemoveField(
            model_name='service',
            name='product_name',
        ),
    ]