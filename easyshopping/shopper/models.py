from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

CATEGORIES = [
    ('Искусство', 'Искусство'),
    ('Цифровые товары', 'Цифровые товары'),
    ('Одежда', 'Одежда')
]


class User(AbstractUser):
    """ Abstract model for each user """
    pass


class Good(models.Model):
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
        upload_to='images',
        null=False,
        blank=True,
        verbose_name='Изображение товара'
    )

    availability = models.BooleanField(
        default=False,
        verbose_name='Доступно на складе'
    )

    categories = models.CharField(
        max_length=255,
        choices=CATEGORIES,
        default='Цифровые товары',
    )

    def __str__(self):
        return f"Товар {self.title}"


class Shop(models.Model):
    """ Represents each unique shop in catalog """

    title = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        verbose_name='Магазин',
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='Ссылка',
        null=False,
        blank=True,
    )

    description = models.TextField(
        null=False,
        blank=True,
        verbose_name='Описание магазина'
    )

    address = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        verbose_name='Адрес магазина',
    )

    contacts = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        verbose_name='Контакты',
    )

    image = models.ImageField(
        upload_to='images',
        null=False,
        blank=True,
        verbose_name='Изображение магазина'
    )

    time_added = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name='Дата добавления'

    )

    def __str__(self):
        return f'Магазин {self.title}'

    def get_absolute_url(self):
        return reverse('shop', kwargs={'shop_slug': self.slug})