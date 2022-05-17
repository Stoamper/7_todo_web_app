from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="имя")
    last_name = models.CharField(max_length=64, verbose_name="фамилия")
    birthday_year = models.PositiveIntegerField(verbose_name="дата рождения", blank=True, null=True)
    email = models.EmailField(max_length=254, verbose_name="электронная почта", unique=True)
    city = models.CharField(max_length=128, default="Москва", verbose_name="город", blank=True, null=True)
    address = models.CharField(max_length=254, verbose_name="адресс", blank=True, null=True)