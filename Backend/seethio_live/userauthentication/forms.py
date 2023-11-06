from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.password_validation import validate_password

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


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "New Password",
                "class": "custom-input-class",  # Add your custom CSS class here
                "id": "password",
            }
        ),
        validators=[validate_password],
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Re-type Password",
                "class": "custom-input-class",  # Add your custom CSS class here
                "id": "password",
            }
        ),
        validators=[validate_password],
    )
    error_messages = {
        "password_mismatch": ("The two password fields didn't match."),
    }




class OTPVerificationForm(forms.Form):
    otp = forms.CharField(
        label="Enter OTP",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the OTP sent to your email"}
        ),
        max_length=6,
    )