from django import forms
from django.forms import ModelForm
from .models import Part, Product, PartPack


class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = "__all__"
        labels = {
            'part_name': '',
            'part_supplier_name': '',
            'part_supplier_phone': '',
            'part_supplier_address': '',
            'part_description': '',
        }
        widgets = {
            'part_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام قطعه'}),
            'part_supplier_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام تامین کننده'}),
            'part_supplier_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن تامین کننده'}),
            'part_supplier_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس تامین کننده'}),
            'part_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات قطعه'}),
        }


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
        fields = ['product_name', 'part_name', 'part_quantity', 'part_price', 'part_repair_cost', 'part_repair_customer_site']
        labels = {
            'product_name': 'نام محصول',
            'part_name': 'نام قطعه',
            'part_price': 'قیمت فروش قطعه',
            'part_quantity': 'تعداد مورد نیاز',
            'part_repair_cost': 'دستمزد تعویض',
            'part_repair_customer_site': 'امکان تعویض در محل مشتری' ,
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
