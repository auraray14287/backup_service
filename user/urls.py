from django.urls import path
from .views import user_dashboard, user_profiles, backed_up_files, restore_files, admin_dashboard

urlpatterns = [
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('profiles/', user_profiles, name='user_profiles'),
    path('backed-up-files/', backed_up_files, name='backed_up_files'),
    path('restore-files/', restore_files, name='restore_files'),
    path('admin/dashboard/<int:user_id>/', admin_dashboard, name='admin_dashboard'),
    # Add other user-related URLs
]
