# Built-in libraries
from uuid import uuid4
# Framework libraries
from django.db import models
# Other libraries
# Project libraries


class BaseModel(models.Model):
    id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True