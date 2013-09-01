from django import forms

from ajax_select.fields import AutoCompleteSelectField

from apps.products.models import Product


class OperationProductForm(forms.Form):
    product = AutoCompleteSelectField('product')
    quantity = forms.IntegerField()

    def __init__(self, operation='addition', *args, **kwargs):
        super(OperationProductForm, self).__init__(*args, **kwargs)
        self.operation = operation

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
