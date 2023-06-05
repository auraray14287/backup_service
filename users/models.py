from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission

class User(AbstractUser, PermissionsMixin):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    staff_id = models.CharField(max_length=10, blank=True, null= True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, default=None, null=True)
    mobile =models.CharField(default='',max_length=15,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    storage_paths = models.TextField()  # Store multiple storage paths as a comma-separated string

    def get_storage_paths(self):
        return self.storage_paths.split(',')

    def set_storage_paths(self, paths):
        self.storage_paths = ','.join(paths)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class BackupFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storage_path = models.CharField(max_length=255)
    file = models.FileField(upload_to='backups/')
    extension = models.CharField(max_length=50)
    backup_date = models.DateTimeField(auto_now_add=True)


