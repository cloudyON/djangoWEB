from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.logistics.models import Product


class ProductAdmin(SimpleHistoryAdmin):
    list_display = ('paymentWay', 'ordererPay', 'cardName', 'point')
    history_list_display = ('paymentWay', 'ordererPay', 'cardName', 'point')
    search_fields = ['paymentWay', 'name']

admin.site.register(Product, ProductAdmin)