from django.contrib import admin
from django.contrib import admin
from django.core.management import call_command
from .backup import BackupCommand

# Register the BackupCommand in Django's management commands
call_command('register', BackupCommand())

# Register your other models here

# Register your models here.
