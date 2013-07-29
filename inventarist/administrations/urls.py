from django.conf.urls import patterns, url

urlpatterns = patterns('inventarist.administrations.views',
    url(r'^product-operation/(?P<operation>addition|substraction)$', 'product_operation', name='product_operation')
)
