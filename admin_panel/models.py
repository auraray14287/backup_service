from django.db import models
from users.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class FileExtension(models.Model):
    extension = models.CharField(max_length=50)
