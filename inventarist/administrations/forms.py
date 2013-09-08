from django import forms
from django.contrib.admin import widgets

from ajax_select.fields import AutoCompleteSelectField

from .utils import generate_product_report


class OperationProductForm(forms.Form):
    product = AutoCompleteSelectField('product')
    quantity = forms.IntegerField()

    def __init__(self, operation='addition', *args, **kwargs):
        super(OperationProductForm, self).__init__(*args, **kwargs)
        self.operation = operation

    def clean(self):
        cleaned_data = super(OperationProductForm, self).clean()
        product = cleaned_data['product']
        quantity = cleaned_data['quantity']
        if self.operation == 'substraction':
            quantity = -1 * quantity

        if product.quantity + quantity < 0:
            raise forms.ValidationError("Hasil akhir tidak boleh dibawah 0")

        return cleaned_data

    def save(self, *args, **kwargs):
        quantity = self.cleaned_data['quantity']
        if self.operation == 'substraction':
            quantity = -1 * quantity

        product = self.cleaned_data['product']
        self.quantity_was = product.quantity
        self.operation_quantity = quantity
        product.quantity += quantity
        product.save()
        return product

class ProductReportForm(forms.Form):
    start_date = forms.DateField(widget=widgets.AdminDateWidget(), required=True)
    end_date = forms.DateField(widget=widgets.AdminDateWidget(), required=True)


    def generate_report(self):
        generate_product_report(self.cleaned_data['start_date'], self.cleaned_data['end_date'])
