from django.db import models
from registration.models import CustomUser


class Department(models.Model):
    # Поля департамента
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Управление"
        verbose_name_plural = "Управления"


class Division(models.Model):
    # Поля отдела
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Управление')
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.name


class Sector(models.Model):
    # Поля сектора
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name='Отдел')
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta ():
        verbose_name = "Сектор"
        verbose_name_plural = "Сектора"

    def __str__(self):
        return self.name


class UserSectorAccess(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, verbose_name='Сектор')

    def __str__(self):
        return f"User: {self.user.username}, Sector: {self.sector.name}"
    class Meta ():
        verbose_name = "Доступ к сетору"
        verbose_name_plural = "Доступ к сеторам"


class UserDivisionAccess(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name='Отдел')

    def __str__(self):
        return f"User: {self.user.username}, Division: {self.division.name}"
    class Meta ():
        verbose_name = "Доступ к отделам"
        verbose_name_plural = "Доступ к отделу"
