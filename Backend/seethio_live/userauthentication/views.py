from django.urls import reverse
from django.shortcuts import redirect, render
from userauthentication.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
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