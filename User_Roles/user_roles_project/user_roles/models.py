# user_roles/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    roles = models.ManyToManyField('Role', through='UserRole', related_name='users')

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"


class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"