"""
URL configuration for seethio_live project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from userauthentication.views import home
from userauthentication import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new from render deploy


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("userauthentication.urls")),
    path("Booking/", include("Booking.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('auth/', include('social_django.urls', namespace='social')), # Social authentication by
 
    ]

urlpatterns += staticfiles_urlpatterns() # new for render deploy

