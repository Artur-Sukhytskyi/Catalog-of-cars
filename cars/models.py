from django.db import models

# Create your models here.

from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    T_CHOICES = (
        (1, 'Механическая коробка передач'),
        (2, 'Автоматическая коробка передач'),
        (3, 'Роботизированная коробка передач'),
    )
    C_CHOICES = (
        (1, 'Красный'),
        (2, 'Оранжевый'),
        (3, 'Жёлтый'),
        (4, 'Зелёный'),
        (5, 'Голубой'),
        (6, 'Синий'),
        (7, 'Фиолетовый'),
        (8, 'Белый'),
        (9, 'Чёрный'),
    )

    vendor = models.CharField(max_length=50,
                              verbose_name='Производитель')
    model = models.CharField(max_length=50,
                             verbose_name='Модель авто')
    year = models.IntegerField(validators=[MinValueValidator(1900),
                                           MaxValueValidator(2020)],
                               verbose_name='Год выпуска')
    transmission = models.SmallIntegerField(choices=T_CHOICES,
                                            default=1,
                                            verbose_name='Коробка передач')
    color = models.SmallIntegerField(choices=C_CHOICES,
                                     verbose_name='Цвет',
                                     default=1)

    def __str__(self):
        return f'Автомобиль {self.model} марки {self.vendor}'

    class Meta:
        ordering = ('vendor', 'model',)