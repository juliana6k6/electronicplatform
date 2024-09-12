from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя с авторизацией по email"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Емейл', help_text="Введите электронную почту")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        help_text="Введите имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
        help_text="Введите фамилию",
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        help_text="Укажите ваш телефон",
        blank=True, null=True
    )
    is_active = models.BooleanField(default=True, verbose_name="активный пользователь")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
