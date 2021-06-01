from django.contrib import admin

from apps.proxies.models import Proxy


@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'is_enable')
    search_fields = ('host',)
    list_filter = ('is_enable',)
