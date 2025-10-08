import uuid

from django.db import models


# Create your models here.
class AppUser(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=str(uuid.uuid4), editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class AppUserProfile(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=str(uuid.uuid4), editable=False)
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
