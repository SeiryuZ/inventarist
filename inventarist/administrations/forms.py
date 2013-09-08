from django import forms

from ajax_select.fields import AutoCompleteSelectField


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
