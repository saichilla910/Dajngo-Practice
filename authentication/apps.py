from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'authentication'
    def ready(self):
        from . import signals
