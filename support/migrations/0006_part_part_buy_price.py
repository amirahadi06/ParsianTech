# Generated by Django 3.2.6 on 2021-10-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_auto_20211010_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='part_buy_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Part Buy Price'),
        ),
    ]
