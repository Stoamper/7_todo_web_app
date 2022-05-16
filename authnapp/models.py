from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="имя")
    last_name = models.CharField(max_length=64, verbose_name="фамилия")
    birthday_year = models.PositiveIntegerField(verbose_name="дата рождения")
    email = models.EmailField(max_length=254, verbose_name="электронная почта", unique=True)
    city = models.CharField(max_length=128, default="Москва", verbose_name="город")
    address = models.CharField(max_length=254, verbose_name="адресс")