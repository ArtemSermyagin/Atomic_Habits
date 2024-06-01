from datetime import timedelta

from django.core.validators import MaxValueValidator
from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    period = [
        ('week', 'once a week'),
        ('every_day', 'every day')
    ]

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        **NULLABLE
    )
    place = models.CharField(max_length=200, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=200, verbose_name='Действие')
    sign_good_habit = models.BooleanField(
        default=False,
        verbose_name='Признак приятной привычки'
    )
    related_habits = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        **NULLABLE,
        related_name='related',
        verbose_name='Связанная привычка'
    )
    periodicity = models.CharField(
        max_length=20,
        choices=period,
        default='every_day',
        verbose_name="Периодичность"
    )
    reward = models.CharField(max_length=200, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.IntegerField(
        verbose_name='Время на выполнение',
        validators=[MaxValueValidator(int(timedelta(seconds=120).total_seconds()))]
    )
    is_public = models.BooleanField(
        default=True,
        verbose_name="Признак публичности"
    )

    def __str__(self):
        return f'{self.user} будет {self.action} в {self.time} на {self.place}'

    class Meta:
        db_table = 'habits'
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
