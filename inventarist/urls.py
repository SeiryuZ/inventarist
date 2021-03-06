from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventarist.views.home', name='home'),
    # url(r'^inventarist/', include('inventarist.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', RedirectView.as_view(url='/admin/')),
    url(r'^api/', include('inventarist.api.urls', namespace='api')),

    # Add this to get widgets.AdminDateWidget() working for non is_staff, is_superuser
    # This must be placed before (r'^admin/(.*)', admin.site.root), as that gobals up everything
    (r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),

    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administration/', include('inventarist.administrations.urls', namespace='administration')),
)
