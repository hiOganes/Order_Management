# Built-in libraries
from uuid import uuid4
# Framework libraries
from django.db import models
# Other libraries
# Project libraries


class BaseModel(models.Model):
    """
    A base model class that includes common fields and methods for all models.

    Attributes:
        id (UUIDField): Unique identifier for the model instance.
        created_at (DateTimeField): Timestamp when the instance was created.
        updated_at (DateTimeField): Timestamp when the instance was updated.
    """

    id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True