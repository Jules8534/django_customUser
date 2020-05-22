from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    
    home_page = models.URLField(max_length=100, null=True, blank=True)
    user_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    display_name = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['age']
