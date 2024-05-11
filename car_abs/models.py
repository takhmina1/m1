# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class YourUserModel(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

    # Add any other fields or methods you need

    def __str__(self):
        return self.email
