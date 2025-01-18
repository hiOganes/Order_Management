# Built-in libraries
# Framework libraries
from django.db import models
# Other libraries
# Project libraries
from apps.common.models import BaseModel


class Orders(BaseModel):
    class Status(models.TextChoices):
        WAIT = 'В ожидании', 'В ожидании'
        DONE = 'Готово', 'Готово'
        PAID = 'Оплачено','Оплачено'

    table_number = models.IntegerField()
    items = models.JSONField()
    total_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        default=0,
    )
    status = models.CharField(choices=Status.choices, default=Status.WAIT)
