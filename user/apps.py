from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        from .backup import BackupCommand
        from django.core.management import call_command

        # Register the BackupCommand in Django's management commands
        call_command('register', BackupCommand())
