from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    email = forms.CharField(
        widget = forms.EmailInput(attrs={"class":"form-control"}),
        max_length=50,
        required=True
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={"class":"form-control"}),
        max_length=15,
        required=True
    )
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=10, required=False)
    email = forms.EmailField(max_length=50, required=False)
    
    class Meta:
        model = Users
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )