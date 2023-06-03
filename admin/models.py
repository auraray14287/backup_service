from django.db import models
from django.contrib.auth.models import User

class BackupSchedule(models.Model):
    backup_time = models.TimeField()
    frequency = models.CharField(max_length=50)
    # Add more fields as needed for backup schedule configuration

class BackupReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    staff_id = models.CharField(max_length=10)
    # Add more fields for admin profile information
