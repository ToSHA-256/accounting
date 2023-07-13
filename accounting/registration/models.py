from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    wallet = models.DecimalField(max_digits=6, decimal_places=2, default=0)  # кошелёк

    def __str__(self):
        return self.username
