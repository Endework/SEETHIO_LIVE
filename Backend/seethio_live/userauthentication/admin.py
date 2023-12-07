from django.contrib import admin
from .models import User, Subscribers

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display =['username', 'email']

admin.site.register(User, UserAdmin)
admin.site.register(Subscribers)