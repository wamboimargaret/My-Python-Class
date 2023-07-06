from django.contrib import admin

# Register your models here.

from.models import User_Login
class UserloginAdmin(admin.ModelAdmin):
    list_display = ("user_name", "email", "password", "first_name", "last_name", "phone_number", "date_of_birth")

admin.site.register(User_Login, UserloginAdmin)