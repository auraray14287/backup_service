from django import forms
from .models import UserProfile, BackedUpFile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'last_name','staff_id','department']

class BackedUpFileForm(forms.ModelForm):
    class Meta:
        model = BackedUpFile
        fields = ['name', 'file']
