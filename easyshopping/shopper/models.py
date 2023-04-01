from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    """ Abstract model for each user """
    pass

class Good:
    """ Model which represents each item in shop """

    title = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        verbose_name='Название товара',
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена товара',
        null=False,
        blank=True,
        validators=[MinValueValidator(10), MaxValueValidator(999999)],
    )

    description = models.TextField(
        null=False,
        blank=True,
        verbose_name='Описание',
    )

    image = models.ImageField(
        upload_to='/images',
        null=False,
        blank=True,
    )

    availability = models.BooleanField(
        default=False,
    )