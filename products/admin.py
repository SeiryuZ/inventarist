from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'limit')

    # fields = ['name', 'quantity', 'limit']


admin.site.register(Product, ProductAdmin)
