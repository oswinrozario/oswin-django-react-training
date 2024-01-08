from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
