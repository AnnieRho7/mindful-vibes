from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
import re

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

    def clean_first_name(self):
        """Validate first name contains only letters"""
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            if not first_name.replace(' ', '').isalpha():
                raise forms.ValidationError(
                    "First name should only contain letters"
                )
        return first_name

    def clean_last_name(self):
        """Validate last name contains only letters"""
        last_name = self.cleaned_data.get('last_name')
        if last_name:
            if not last_name.replace(' ', '').isalpha():
                raise forms.ValidationError(
                    "Last name should only contain letters"
                )
        return last_name


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
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'maxlength': 500
                }
            ),
            'profile_image': forms.FileInput(
                attrs={'class': 'form-control-file'}
            ),
        }

    def clean_bio(self):
        """Validate bio length"""
        bio = self.cleaned_data.get('bio')
        if bio and len(bio) > 500:
            raise forms.ValidationError(
                "Bio cannot be longer than 500 characters"
            )
        return bio