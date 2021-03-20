# Register your models here.
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.payment.models import Payment

class PaymentAdmin(SimpleHistoryAdmin):
    list_display = ('paymentWay', 'ordererPay', 'cardName', 'point')
    history_list_display = ('paymentWay', 'ordererPay', 'cardName', 'point')
    search_fields = ['pd_num', 'name']

admin.site.register(Payment, PaymentAdmin)
