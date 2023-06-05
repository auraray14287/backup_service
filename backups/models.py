from django.db import models
from users.models import User

class Backup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule_time = models.TimeField()
    is_active = models.BooleanField(default=True)

class BackupLog(models.Model):
    backup = models.ForeignKey(Backup, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)

class BackupFile(models.Model):
    backup = models.ForeignKey(Backup, on_delete=models.CASCADE, related_name='files')
    storage_path = models.CharField(max_length=255)
    file = models.FileField(upload_to='backups/')
    extension = models.CharField(max_length=50)
    backup_date = models.DateTimeField(auto_now_add=True)
