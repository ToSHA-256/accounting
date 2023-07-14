from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

    class Meta():
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
