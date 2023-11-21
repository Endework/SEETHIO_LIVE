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
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required # aded by ogo
from social_django.utils import psa #added by ogo
from django.contrib.auth import logout as auth_logout  # Renamed to avoid conflict

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
#flight views of amadeus



User = get_user_model()

# User = settings.AUTH_USER_MODEL


# Create your views here.
def index(request):
    return render(request, "Html/index.html")

def home(request):
    return render(request, "Html/Home.html")



def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email_verification, created = EmailVerification.objects.get_or_create(user=user)
            email_verification.generate_otp()
            email_verification.save()

            # Send an email with OTP
            subject = "Verify Your Email And Join The Seethio Adventurers"
            message = f"Hello {user.username} \n\n You're one step closer to joining our community of adventurers exploring Ethiopia's rich cultures and seeking thrilling experiences. \n\n To unlock your adventure, please Enter this verification code: {email_verification.otp} \n\n Once confirmed, you'll officially join the Seethio Adventurers, unlocking exclusive deals, discounts, and rewards. \n\n Don't miss out on this adventure of a lifetime. Confirm your email now for amazing fun! \n\n Thanks for choosing us, \n The Seethio Team."
            from_email = "seethiolive@mail.com"  # Update with your email
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
                    return redirect("userauthentication:home")
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
                            "seethiolive@mail.com",
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
                            "seethiolive@mail.com",  # Change to your email
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

@psa('social:complete')
def google_callback(request):
    # This view will handle the Google callback and log the user in.
    return redirect('Html/Home.html')  # Redirect to your desired page after login.

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from amadeus import Client, ResponseError
from .forms import FlightSearchForm

def search_flights(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            # Retrieve data from the form
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            departure_date = form.cleaned_data['departure_date']

            # Initialize the Amadeus client with your API key
            amadeus = Client(
                client_id='settings.AMADEUS_API_KEY,',
                client_secret='settings.AMADEUS_API_SECRET',
                hostname='test.api.amadeus.com'  # Change to 'api.amadeus.com' for production
            )

            try:
                # Make a request to the Amadeus Flight Offers Search API
                response = amadeus.shopping.flight_offers_search.get(
                    originLocationCode=origin,
                    destinationLocationCode=destination,
                    departureDate=departure_date,
                    adults=1  # Adjust parameters as needed
                )

                # Process the API response and store it in the database or return as JSON
                # (You'll need to adapt this based on the actual Amadeus API response structure and your model)

                # For simplicity, just return the Amadeus API response as JSON
                return JsonResponse(response.data)

            except ResponseError as e:
                # Handle Amadeus API response errors
                return JsonResponse({'error': str(e)})

    else:
        form = FlightSearchForm()

    return render(request, 'search_flights.html', {'form': form})
