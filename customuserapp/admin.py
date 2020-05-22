from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from customuserapp.models import MyUser
# from customuserapp.form import UserCreationForm

# Register your models here.
# 
admin.site.register(MyUser, UserAdmin)
