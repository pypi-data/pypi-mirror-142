from django.apps import AppConfig
from typeidea.custom_site import custom_site

class ConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'config'
