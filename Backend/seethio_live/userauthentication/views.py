from django.urls import reverse
from django.shortcuts import redirect, render
from userauthentication.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from .models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordResetForm

# from django.contrib.auth.models import User as AuthUser
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from .forms import *
from userauthentication.models import EmailVerification
import random
from urllib.parse import unquote

User = get_user_model()

# User = settings.AUTH_USER_MODEL


# Create your views here.
def index(request):
    return render(request, "Html/index.html")


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email_verification, created = EmailVerification.objects.get_or_create(user=user)
            email_verification.generate_otp()
            email_verification.save()

            # Send an email with OTP
            subject = "Email Verification OTP"
            message = f"Your OTP for email verification is: {email_verification.otp}"
            from_email = "your_email@example.com"  # Update with your email
            to_email = user.email

            try:
                send_mail(subject, message, from_email, [to_email])
            except Exception as e:
                messages.error(request, "Failed to send email with OTP. Please contact support.")
                return redirect("userauthentication:signup")

            # Encode user.id for the URL
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            return render(request, "Html/Signup/sign_up_successful.html", {"uidb64": uidb64})

    else:
        form = UserRegisterForm()

    context = {
        "form": form,
    }
    return render(request, "Html/Signup/Signup.html", context)


def sign_success(request):
    return render(request, "Html/Signup/sign_up_successful.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            if user.email_verified:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You are logged in successfully")
                    return redirect("userauthentication:index")
                else:
                    messages.warning(request, "Incorrect password")
            else:
                messages.warning(request, "Email is not verified. Please check your email for the OTP.")
        except User.DoesNotExist:
            messages.warning(request, f"User with {email} does not exist")

    return render(request, "Html/Login/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("userauthentication:signin")


def password_reset_request(request):
    if request.method == "POST":
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data["email"]
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.txt"
                    parameter = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, parameter)
                    try:
                        send_mail(
                            subject,
                            email,
                            "smartcash565@gmail.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except Exception as e:
                        print("Error sending email:", str(e))
                        return HttpResponse("Error sending email")
                    return redirect("userauthentication:password_reset_done")
            else:
                # return HttpResponse("Email does not exist")
                messages.warning(
                    request, "Email address does not exist, please try again"
                )
                # password_form = PasswordResetForm()
    else:
        password_form = PasswordResetForm()

    context = {
        "password_form": password_form,
    }
    return render(request, "registration/password_reset_form.html", context)


def reset_password(request):
    if request.method == "POST":
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            # Reset the user's password
            new_password = form.cleaned_data['new_password1']  # Get the new password
            user = request.user  # Assuming the user is authenticated
            user.set_password(new_password)
            user.save()

            # Redirect to the password reset complete page
            return redirect("userauthentication:password_reset_complete")

    else:
        form = SetPasswordForm()

    return render(request, "password_reset_confirm.html", {"form": form})


def verify_email(request, uidb64):
    if request.method == "POST":
        otp_parts = []
        for i in range(1, 7):
            input_name = f"otp{i}"
            otp_part = request.POST.get(input_name)
            if otp_part:
                otp_parts.append(otp_part)

        otp = "".join(otp_parts)

        # Decode the URL parameter
        decoded_uidb64 = unquote(uidb64)
        user_id = urlsafe_base64_decode(decoded_uidb64)

        user = User.objects.get(pk=user_id)
        email_verification = EmailVerification.objects.get(user=user)

        if email_verification.otp == otp:
            email_verification.verified = True
            email_verification.save()
            user.email_verified = True
            user.save()
            messages.success(request, "Email verification successful. You can now log in.")
            return redirect("userauthentication:email_verification_complete")
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    else:
        otp_form = OTPVerificationForm()
        context = {
            "otp_form": otp_form,
            "uidb64": uidb64,
        }
        return render(request, "Html/Signup/verification.html", context)


def email_verification_complete(request):
    return render(request, "Html/Signup/Email_verification_complete.html")

def resend_password_reset_email(request):
    if request.method == "POST":
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data["email"]
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    # Generate a password reset email and send it to the user
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.txt"
                    parameter = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",  # Change to your domain
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, parameter)
                    try:
                        send_mail(
                            subject,
                            email,
                            "smartcash565@gmail.com",  # Change to your email
                            [user.email],
                            fail_silently=False,
                        )
                    except Exception as e:
                        print("Error sending email:", str(e))
                        return HttpResponse("Error sending email")
                    return redirect("userauthentication:password_reset_done")
            else:
                messages.warning(
                    request, "Email address does not exist, please try again"
                )
    else:
        password_form = PasswordResetForm()

    context = {
        "password_form": password_form,
    }
    return render(request, "registration/password_reset_form.html", context)