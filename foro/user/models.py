from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255)

class Profile(models.Model):
    