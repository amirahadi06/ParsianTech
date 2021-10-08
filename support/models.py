from django.db import models
from django.utils.translation import gettext as _


class Part(models.Model):
    part_name = models.CharField(verbose_name=_('Part Name'), max_length=100)
    part_supplier_name = models.CharField(verbose_name=_('Part Supplier Name'), max_length=100, blank=True)
    part_supplier_phone = models.CharField(verbose_name=_('Part Supplier Phone'), max_length=20, blank=True)
    part_supplier_address = models.CharField(verbose_name=_('Part Supplier Address'), max_length=400, blank=True)
    part_description = models.TextField(verbose_name=_('Part Description'), max_length=1000, blank=True)

    class Meta:
        verbose_name = _('Part')
        verbose_name_plural = _('Parts')

    def __str__(self):
        return self.part_name


class Product(models.Model):

    product_models = (
        ('BASIC', 'BASIC'),
        ('ECO', 'ECONOMY'),
        ('PRO', 'PROFESSIONAL'),
        ('FULL', 'FULL'),
    )

    product_name = models.CharField(verbose_name=_('product name'), max_length=200)
    product_model = models.CharField(verbose_name=_('Product model'), max_length=200, choices=product_models, default='eco')
    product_part = models.ManyToManyField(Part, through='PartPack', blank=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return "%s (%s)" % (self.product_name, self.product_model)


class PartPack(models.Model):
    part_name = models.ForeignKey(Part, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    part_quantity = models.IntegerField(default=1, blank=True)
    part_repair_cost = models.IntegerField(default=0, blank=True)

    class Meta:
        verbose_name = _('Part Pack')
        verbose_name_plural = _('Part Packs')

    def __str__(self):
        return "%s (%s)" % (self.part_name, self.product_name)


class Customer(models.Model):
    customer_company_name = models.CharField(verbose_name=_('customer company name'), max_length=200)
    customer_product = models.ManyToManyField(Product, through='ProductOwnership')

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return self.customer_company_name


class ProductOwnership(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_serial_number = models.IntegerField()

    def __str__(self):
        return "%s (%s)" % (self.product_name, self.product_serial_number)


class Contact(models.Model):
    contact_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_name = models.CharField(verbose_name=_('contact_name'), max_length=200)
    contact_position = models.CharField(verbose_name=_('contact_position'), max_length=200)
    contact_mobile = models.CharField(verbose_name=_('contact_mobile'), max_length=200)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.contact_name


class Service(models.Model):
    customer_service = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # product_name =
    description = models.TextField()

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.description

