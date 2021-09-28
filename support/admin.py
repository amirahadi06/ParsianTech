from django.contrib import admin
from .models import Customer, Product, Part, Service, Contact

admin.site.register(Part)


# ------------------------------------------


class PartInline(admin.TabularInline):
    model = Product.product_part.through
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PartInline]


admin.site.register(Product, ProductAdmin)


# ------------------------------------------


class ContactsInLine(admin.TabularInline):
    model = Contact
    extra = 0


class ProductInLine(admin.TabularInline):
    model = Customer.customer_product.through
    extra = 0


class ServiceInLine(admin.TabularInline):
    model = Service
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    inlines = [ContactsInLine, ProductInLine, ServiceInLine]


admin.site.register(Customer, CustomerAdmin)
