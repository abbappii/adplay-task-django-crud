from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from user.models import UserProfile

User = get_user_model()


class UserProfileForm(ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']


class CreateUserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']
