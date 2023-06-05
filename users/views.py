from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.has_perm('admin_panel.access_admin_dashboard'):
                    return redirect(reverse('users:admin_dashboard'))
                else:
                    return redirect(reverse('users:user_dashboard'))
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def user_dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def user_profile(request):
    return render(request, 'users/profile.html')

@login_required
def backed_up_files(request):
    return render(request, 'users/backed_up_files.html')

@login_required
def restore_files(request):
    return render(request, 'users/restore_files.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('users:login'))

@login_required
def admin_dashboard(request):
    # Check if the user has permission to access the admin dashboard, otherwise redirect to user_dashboard
    if not request.user.has_perm('admin_panel.access_admin_dashboard'):
        messages.error(request, 'You do not have permission to access the admin dashboard.')
        return redirect(reverse('users:user_dashboard'))

    return render(request, 'users/admin_dashboard.html')

@login_required
def users_report(request):
    # Check if the user has permission to access the users report, otherwise redirect to user_dashboard
    if not request.user.has_perm('admin_panel.view_users_report'):
        messages.error(request, 'You do not have permission to access this page.')
        return redirect(reverse('users:user_dashboard'))

    return render(request, 'users/users_report.html')

@login_required
def backup_report(request):
    # Check if the user has permission to access the backup report, otherwise redirect to user_dashboard
    if not request.user.has_perm('admin_panel.view_backup_report'):
        messages.error(request, 'You do not have permission to access this page.')
        return redirect(reverse('users:user_dashboard'))

    return render(request, 'users/backup_report.html')

@login_required
def settings(request):
    # Check if the user has permission to access the settings page, otherwise redirect to user_dashboard
    if not request.user.has_perm('admin_panel.view_settings'):
        messages.error(request, 'You do not have permission to access this page.')
        return redirect(reverse('users:user_dashboard'))

    return render(request, 'users/settings.html')
