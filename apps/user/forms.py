from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
    
        model = UserProfile
        fields = ('username',)


class UserProfileChangeForm(UserChangeForm):
    password = None

    class Meta(UserCreationForm.Meta):
    
        model = UserProfile
        fields = ('email', 'first_name', 'last_name', 'avatar')