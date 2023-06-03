from django.shortcuts import render
from user.models import BackedUpFile

def dashboard(request):
    # Implement view for the admin dashboard
    return render(request, 'admin/dashboard.html')

def backup_settings(request):
    # Implement view for backup settings
    return render(request, 'admin/backup_settings.html')

def backup_schedule(request):
    # Implement view for backup schedule configuration
    return render(request, 'admin/backup_schedule.html')

def backup_reports(request):
    # Get the list of backup reports
    reports = BackedUpFile.objects.all()
    return render(request, 'admin/backup_reports.html', {'reports': reports})
