from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatar/', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    telegram_chat_id = models.CharField(max_length=100, verbose_name='ID в телеграме', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
