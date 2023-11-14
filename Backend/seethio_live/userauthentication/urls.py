from django.urls import path
from userauthentication.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView
from userauthentication.forms import CustomSetPasswordForm

app_name = "userauthentication"
urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),
    path("verify_email/<str:uidb64>/", verify_email, name="verify_email"),
    path("signup/", register_view, name="signup"),
    path("sign_success/", sign_success, name="sign_success"),
    path("signin/", login_view, name="signin"),
    path("email_verification_complete/", email_verification_complete, name="email_verification_complete"),
    path("signout/", logout_view, name="signout"),
    path('resend_password_reset_email/', resend_password_reset_email, name='resend_password_reset_email'),
    path("password_reset/", password_reset_request, name="password_reset"),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
     path(
        'password_reset/confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            form_class=CustomSetPasswordForm
        ),
        name='password_reset_confirm',
    ),
    path(
        "password_reset_complete",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]