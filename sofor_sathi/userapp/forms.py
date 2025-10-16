from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('password2'):
            self.add_error('password2', "Passwords do not match.")
        return cleaned


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio','profile_pic','language_preference','travel_preference')
