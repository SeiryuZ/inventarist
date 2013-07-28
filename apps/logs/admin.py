from django.contrib import admin
from django.utils.timezone import localtime
from apps.logs.models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'product', 'format_created')

    def format_created(self, obj):
        return localtime(obj.created).strftime('%d %b %Y %H:%M')

    format_created.short_description = 'Created at'
    format_created.admin_order_field = 'created'

admin.site.register(Log, LogAdmin)
