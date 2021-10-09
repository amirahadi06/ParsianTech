from django import forms
from django.forms import ModelForm
from .models import Part, Product, PartPack, Supplier


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        labels = {
            'supplier_name': '',
            'supplier_phone': '',
            'supplier_address': '',
            'supplier_description': '',
        }
        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام تامین کننده'}),
            'supplier_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن تامین کننده'}),
            'supplier_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس تامین کننده'}),
            'supplier_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات'}),
        }


class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = ['part_name', 'part_description', 'part_supplier', 'part_buy_price']
        labels = {
            'part_name': '',
            'part_buy_price': 'قیمت خرید',
            'part_supplier': 'تامین کننده',
            'part_description': '',
        }
        widgets = {
            'part_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام قطعه'}),
            'part_buy_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'قیمت خرید(تومان)'}),
            'part_supplier': forms.Select(attrs={'class': 'form-select', 'placeholder': 'تامین کننده'}),
            'part_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات قطعه'}),
        }

    def __init__(self, *args, **kwargs):
        super(PartForm, self).__init__(*args, **kwargs)
        self.fields['part_supplier'].empty_label = 'متفرقه'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_model']
        labels = {
            'product_name': '',
            'product_model': '',
            'product_part': 'لیست قطعات به کار رفته در محصول',
        }
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام محصول'}),
            'product_model': forms.Select(attrs={'class': 'form-select', 'selected': 'مدل محصول'}),
            'product_part': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': ''}),
        }


class PartPackForm(ModelForm):
    class Meta:
        model = PartPack
        fields = ['product_name', 'part_name', 'part_quantity', 'part_price', 'part_repair_cost',
                  'part_repair_customer_site']
        labels = {
            'product_name': 'نام محصول',
            'part_name': 'نام قطعه',
            'part_price': 'قیمت فروش قطعه',
            'part_quantity': 'تعداد مورد نیاز',
            'part_repair_cost': 'دستمزد تعویض',
            'part_repair_customer_site': 'امکان تعویض در محل مشتری',
        }
        widgets = {
            'product_name': forms.HiddenInput(attrs={'class': 'form-control'}),
            'part_name': forms.Select(attrs={'class': 'form-select'}),
            'part_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'part_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'part_repair_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'part_repair_customer_site': forms.CheckboxInput(attrs={'class': 'form-check'}),

        }

    def __init__(self, *args, **kwargs):
        super(PartPackForm, self).__init__(*args, **kwargs)
        self.fields['part_name'].empty_label = None
