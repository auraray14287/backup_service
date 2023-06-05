from django.contrib import admin
from .models import Backup, BackupLog, BackupFile

admin.site.register(Backup)
admin.site.register(BackupLog)
admin.site.register(BackupFile)
