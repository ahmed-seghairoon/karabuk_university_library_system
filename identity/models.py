from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_STUDENT = 'student'
    ROLE_ADMIN = 'admin'

    ROLE_CHOICES = [
        (ROLE_STUDENT, 'student'),
        (ROLE_ADMIN, 'admin'),
    ]

    role = models.CharField(max_length=256, choices=ROLE_CHOICES, null=True)