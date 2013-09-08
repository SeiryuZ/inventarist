from django.conf.urls import patterns, url

urlpatterns = patterns('inventarist.administrations.views',
    url(r'^product-operation/(?P<operation>addition|substraction)$', 'product_operation', name='product_operation'),
    url(r'^product-report$', 'product_report', name='product_report')

)
