# Built-in libraries
# Framework libraries
from django.apps import AppConfig
# Other libraries
# Project libraries


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.common'
