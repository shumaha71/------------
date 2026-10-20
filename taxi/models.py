from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

class Profile(models.Model):
    class Role(models.TextChoices):
        PASSENGER = 'passenger', 'Пассажир'
        DRIVER = 'driver', 'Водитель'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь',
    )

    role = models.CharField(
         max_length=20,
         choices=Role.choices,
         default=Role.PASSENGER,
         verbose_name='Роль',
    )

    class Meta:
         verbose_name = 'Профиль'
         verbose_name_plural = 'Профили'

    def __str__(self):
         return f"{self.user.username} - {self.get_role_display()}"

class Tariff(models.Model):
    name = models.CharField(
          max_length=50,
          unique=True,
          verbose_name='Название',
    )
    
    base_price = models.DecimalField(
         max_digits=8,
         decimal_places=2,
         validators=[MinValueValidator(0)],
         verbose_name='Стоимость подачи',
    )

    price_per_km = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Цена за километр',
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Доступен для заказа',
    )

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
        ordering = ['base_price']

    def __str__(self):
        return self.name
    