from django.urls import path
from userauthentication.views import *
from django.contrib.auth import views as auth_views
from . import views #added by ple

app_name = "userauthentication"
urlpatterns = [
    path("", index, name="index"),
    path("signup/", register_view, name="signup"),
    path("sign_success/", sign_success, name="sign_success"),
    path("signin", login_view, name="signin"),
    path("signout", logout_view, name="signout"),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "subscription/", views.subscription, name="subscription"  #added by ple
    ),
]