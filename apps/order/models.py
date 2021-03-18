from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel
from simple_history.models import HistoricalRecords


class Order(TimeStampedModel):
    class Status(models.TextChoices):
        Pending = 'pending'
        Making = 'making'
        Complete = 'complete'


    status = models.CharField('주문상태',choices=Status.choices ,max_length=8, default='pending')
    make_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='makeby_set')
    complete_at = models.DateTimeField( '주문완료시점',null=True)
    orderer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = 'orderer_set')
    product = models.ForeignKey('logistics.Product', on_delete=models.DO_NOTHING)
    complain = models.CharField('불편사항',max_length=200, blank=True)

    history = HistoricalRecords(
        history_change_reason_field=models.TextField(null=True)
    )


    class Meta:
        verbose_name = '주문'
        verbose_name_plural = '주문 리스트'

    def __str__(self):
        return f'{self.id} {self.orderer.username}'

