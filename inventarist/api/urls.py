from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^products', include('inventarist.api.products.urls', namespace='products')),
    url(r'^products/', include('inventarist.api.products.urls', namespace='products'))
)

