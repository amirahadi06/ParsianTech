# Generated by Django 3.2.6 on 2021-10-08 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_auto_20211007_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='partpack',
            name='part_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='partpack',
            name='part_repair_customer_site',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
