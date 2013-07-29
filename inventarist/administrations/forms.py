from django import forms

from apps.products.models import Product


class OperationProductForm(forms.Form):
    product = forms.IntegerField()
    quantity = forms.IntegerField()

    def __init__(self, operation='addition', *args, **kwargs):
        super(OperationProductForm, self).__init__(*args, **kwargs)
        self.operation = operation

    def clean_product(self):
        product = self.cleaned_data['product']
        try:
            product = Product.objects.get(id=product)
            return product
        except Product.DoesNotExist:
            raise forms.ValidationError("Product can't be found")
        return None

    def save(self, *args, **kwargs):
        quantity = self.cleaned_data['quantity']
        if self.operation == 'substraction':
            quantity = -1 * quantity

        product = self.cleaned_data['product']
        product.quantity += quantity
        product.save()
        return product
