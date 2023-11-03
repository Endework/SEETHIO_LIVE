from django import forms
from django.contrib.auth.forms import UserCreationForm

from userauthentication.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Sara"}), required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "jon"}), required=True
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username is Optional"}),
        required=False,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "example@gmail.com"}),
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "********", "id": "password1"}
        ),
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "********"}), required=True
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]