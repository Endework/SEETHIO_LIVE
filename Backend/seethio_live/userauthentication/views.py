from django.urls import reverse
from django.shortcuts import redirect, render
from userauthentication.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required # aded by ogo
from social_django.utils import psa #added by ogo
from django.contrib.auth import logout as auth_logout  # Renamed to avoid conflict
from django.contrib import messages
from django.conf import settings
from mailchimp_marketing import Client #added by ple
from mailchimp_marketing.api_client import ApiClientError #added by ple
from .models import User

# User = settings.AUTH_USER_MODEL


# Create your views here.
def index(request):
    return render(request, "Html/index.html")


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")  # Corrected field name
            messages.success(
                request, f"Hey {username}, your account was created successfully"
            )
            return redirect("userauthentication:sign_success")
    else:
        form = UserRegisterForm()

    context = {
        "form": form,
    }
    return render(request, "Html/Signup/Signup.html", context)


def sign_success(request):
    return render(request, "Html/Signup/sign_up_successful.html")


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey, you are already logged In")
        return redirect("userauthentication:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in successfuly")
                return redirect("userauthentication:index")
            else:
                messages.warning(request, "User Does Not Exist, Sign Up")
        except:
            messages.warning(request, f"User with {email} does not exist")

    return render(request, "Html/Login/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("userauthentication:signin")

@psa('social:complete')
def google_callback(request):
    # This view will handle the Google callback and log the user in.
    return redirect('Html/index.html')  # Redirect to your desired page after login.

# Mailchimp Settings added by ple
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


# Subscription Logic
def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))




# Views here.
def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        subscribe(email)                    # function to access mailchimp
        messages.success(request, "Email received. thank You! ") # message

    return render(request, "Html/index.html")



