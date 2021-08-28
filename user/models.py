from django.db import models
from django.contrib.auth.models import AbstractUser

# 1.	Create Model for user profile (date_of_birth, gender, phone, address)
# 2.	Create User and User Profile
# 3.	List User Profile
# 4.	Update User Profile
# 5.	Delete User Profile


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
