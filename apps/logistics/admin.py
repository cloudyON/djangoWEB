from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.order.models import Order


class OrderAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'status', 'make_by', 'orderer', 'product')
    search_fields = ['product', 'orderer']


admin.site.register(Order, OrderAdmin)
