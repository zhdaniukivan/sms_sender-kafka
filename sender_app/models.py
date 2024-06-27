from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    email = models.CharField(max_length=250, unique=True)

    REQUIRED_FIELDS = ['email']



# Create your models here.
