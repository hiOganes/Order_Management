# Built-in libraries
# Framework libraries
from django.db import models
# Other libraries
# Project libraries
from apps.common.models import BaseModel


class Orders(BaseModel):
    """
    Custom user model extending BaseModel.

    Attributes:
        table_number (int): Table number that makes the order.
        items (json): List of ordered dishes and their prices.
        total_price (decimal): The expected price of the dishes in the order.
        status (str): Order status.

    """

    class Status(models.TextChoices):
        """
        Custom user model extending TextChoices.

        Attributes:
            WAIT (tuple): Order pending.
            DONE (tuple): The order is ready.
            PAID (tuple): The order has been paid.

        """

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
