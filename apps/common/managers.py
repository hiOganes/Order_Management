# Built-in libraries
# Framework libraries
from django.db import models
# Other libraries
# Project libraries


class GetOrNoneQuerySet(models.QuerySet):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNoeExist:
            return None

class GetOrNoneManager(models.Manager):
    def get_queryset(self):
        return GetOrNoneQuerySet(self.model)

    def get_or_none(self, **kwargs):
        return get_queryset.get_or_none(**kwargs)