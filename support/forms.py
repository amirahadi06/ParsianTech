from django import forms
from django.forms import ModelForm
from .models import Part


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
