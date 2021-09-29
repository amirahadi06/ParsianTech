# Generated by Django 3.2.6 on 2021-09-29 23:45

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
                ('customer_company_name', models.CharField(max_length=200, verbose_name='customer company name')),
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
                ('part_name', models.CharField(max_length=100, verbose_name='Part Name')),
                ('part_supplier_name', models.CharField(blank=True, max_length=100, verbose_name='Part Supplier Name')),
                ('part_supplier_phone', models.CharField(blank=True, max_length=20, verbose_name='Part Supplier Phone')),
                ('part_supplier_address', models.CharField(blank=True, max_length=400, verbose_name='Part Supplier Address')),
                ('part_description', models.TextField(blank=True, max_length=1000, verbose_name='Part Description')),
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
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('customer_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.customer')),
            ],
            options={
                'verbose_name': ' سرویس ها ',
                'verbose_name_plural': ' سرویس ها ',
            },
        ),
        migrations.CreateModel(
            name='ProductOwnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_serial_number', models.IntegerField()),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.customer')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.product')),
            ],
        ),
        migrations.AddField(
            model_name='partpack',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_product',
            field=models.ManyToManyField(through='support.ProductOwnership', to='support.Product'),
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
