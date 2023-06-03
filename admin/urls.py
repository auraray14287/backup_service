from django.urls import path
from .views import dashboard, backup_settings, backup_schedule, backup_reports

app_name = 'admin'

urlpatterns = [
    path('dashboard/', dashboard, name='admin_dashboard'),
    path('backupsettings/', backup_settings, name='backup_settings'),
    path('backupschedule/', backup_schedule, name='backup_schedule'),
    path('backupreports/', backup_reports, name='backup_reports'),
    # Add other admin-related URLs
]
