from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    """
    Form for users to update their basic account information.
    Fields: first_name, last_name, email.
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    """
    Form for users to update their profile information.
    Fields: bio, profile_image.
    """
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_image']
        widgets = {
            'bio': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'profile_image': forms.ClearableFileInput(
                attrs={'class': 'form-control-file'}
            ),
        }
