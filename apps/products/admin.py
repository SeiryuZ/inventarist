from django.contrib import admin
from apps.products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'limit')

    def save_model(self, request, obj, form, change):
        action = 2 if change else 1
        obj.logs.create(user=request.user, product=obj, action=action)


admin.site.register(Product, ProductAdmin)
