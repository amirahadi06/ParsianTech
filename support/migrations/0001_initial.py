# Generated by Django 3.2.6 on 2021-09-25 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_company_name', models.CharField(max_length=200, verbose_name='نام شرکت مشتری')),
            ],
            options={
                'verbose_name': ' مشتری ',
                'verbose_name_plural': ' مشتری ',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=200, verbose_name='نام قطعه')),
            ],
            options={
                'verbose_name': 'Part',
                'verbose_name_plural': 'Parts',
            },
        ),
        migrations.CreateModel(
            name='PartPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_quantity', models.IntegerField(default=1)),
                ('part_repair_cost', models.IntegerField()),
                ('part_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.part')),
            ],
            options={
                'verbose_name': 'Part Pack',
                'verbose_name_plural': 'Part Packs',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, verbose_name='product name')),
                ('product_model', models.CharField(max_length=200, verbose_name='Product model')),
                ('product_part', models.ManyToManyField(through='support.PartPack', to='support.Part')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.AddField(
            model_name='partpack',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.product'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200, verbose_name='نام مخاطب')),
                ('contact_position', models.CharField(max_length=200, verbose_name='سمت سازمانی مخاطب')),
                ('contact_mobile', models.CharField(max_length=200, verbose_name='شماره موبایل مخاطب')),
                ('contact_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.customer')),
            ],
            options={
                'verbose_name': ' اطلاعات تماس ',
                'verbose_name_plural': ' اطلاعات تماس ',
            },
        ),
    ]