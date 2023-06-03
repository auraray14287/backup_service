from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username =models.CharField(max_length=100)
    email = models.EmailField()
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    staff_id =models.CharField(max_length=10)
    department =models.CharField(max_length=50)
    # Define additional fields for user profile (e.g., additional info, preferences, etc.)

class BackedUpFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='backups/')
    timestamp = models.DateTimeField(auto_now_add=True)
    # Define additional fields for backed-up files (e.g., filename, timestamp, etc.)