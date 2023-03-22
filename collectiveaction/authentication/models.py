from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Additional user fields, if needed
    pass

    def __str__(self):
        return self.username