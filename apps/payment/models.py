from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Payment(TimeStampedModel):
    class PaymentWay(models.TextChoices):
        Money = "money"
        Credit_card = 'credit card'

    paymentWay = models.CharField('결제 수단', choices=PaymentWay.choices, max_length=20, default='', blank=True)
    ordererPay = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='ordererPay_set', null=True)
    cardName = models.CharField('주문 카드', max_length=30, default=None)
    point = models.IntegerField("포인트", default=None)

    class Meta:
        verbose_name = '주문 처리 관련'
        verbose_name_plural = "주문 관련 리스트"
