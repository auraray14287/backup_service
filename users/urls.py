from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('profile/', views.user_profile, name='user_profile'),
    path('backed-up-files/', views.backed_up_files, name='backed_up_files'),
    path('restore-files/', views.restore_files, name='restore_files'),
    path('logout/', views.user_logout, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users-report/', views.users_report, name='users_report'),
    path('backup-report/', views.backup_report, name='backup_report'),
    path('settings/', views.settings, name='settings'),
]
