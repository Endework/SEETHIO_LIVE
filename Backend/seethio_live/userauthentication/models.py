from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model
import random

# User = get_user_model()

# # Create your models here.
#class User(models.Model):
 #    Userid= models.IntegerField()
  #   username= models.CharField(max_length=50)
   #  email= models.CharField(max_length=100)
    
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)

    def generate_otp(self):
        # Generate a 6-digit OTP
        self.otp = str(random.randint(100000, 999999))
        
# models CREATED BY Ple for signup
class Subscribers(models.Model):
    user_name= models.CharField(max_length=50)
    email_address= models.CharField(max_length=100)
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural= 'Subscribers'


# models CREATED BY OGO for flights

class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    # Add other relevant fields as needed
