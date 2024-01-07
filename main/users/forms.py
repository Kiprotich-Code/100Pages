from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Create your forms here 
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email',]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dp', 'stage_name', 'bio', 'interests',]
