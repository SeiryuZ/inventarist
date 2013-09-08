from django.conf.urls import patterns, url


urlpatterns = patterns('inventarist.api.products.views',
    url(r'^$', 'get_or_create', name="get_or_create"),

    url(r'^(?P<id>\d+)$', 'get', name="get"),

)