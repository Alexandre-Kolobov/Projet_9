from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, through='blog.UserFollows')

    class Meta:
        ordering = ['first_name']
