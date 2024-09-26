from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form for users to submit collaboration requests.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
