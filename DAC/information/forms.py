from django import forms

from .models import Information

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Information
