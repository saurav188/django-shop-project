from django import forms
from django.forms import ModelForm
from user.models import User
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm,UserCreationForm

class user_registration_form(UserCreationForm,forms.Form):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
        ]

class user_info_edit(ModelForm):
    profile_picture=forms.ImageField(required=False)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'profile_picture',
            'phone_no',
            'address',
            'email'
        ]