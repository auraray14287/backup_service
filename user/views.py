from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import UserProfile, BackedUpFile
from .forms import UserProfileForm, BackedUpFileForm


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            # Handle invalid login credentials
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def user_dashboard(request):
    # Implement the user dashboard view
    return render(request, 'user/dashboard.html')

@login_required(login_url='login')
def user_profiles(request):
    profiles = UserProfile.objects.filter(user=request.user)
    return render(request, 'user/profiles.html', {'profiles': profiles})
@login_required(login_url='login')
def backed_up_files(request):
    files = BackedUpFile.objects.filter(user=request.user)
    form = BackedUpFileForm()
    return render(request, 'user/backed_up_files.html', {'files': files, 'form': form})

@login_required(login_url='login')
def restore_files(request):
    # Implement the file restoration logic
    form = BackedUpFileForm()
    return render(request, 'user/restore_files.html', {'form': form})

@staff_member_required(login_url='login')
def admin_dashboard(request):
    # Implement the admin dashboard view
    return render(request, 'admin/dashboard.html')
