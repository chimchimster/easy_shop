from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class ShopperUser(AbstractUser):
    username = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=True,
        verbose_name='Имя пользователя',
    )

    password = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Пароль',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
        verbose_name='Дата регистрации',
    )

    email = models.EmailField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Электронная почта',
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер должен быть в формате: '+999999999' (до 15 символом).",
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'Пользователь {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']


class Products(models.Model):
    p_id = models.IntegerField(
        primary_key=True,
        verbose_name='ID товара'
    )

    p_code = models.IntegerField(
        default=0,
        null=False,
        blank=True,
        verbose_name='Код товара',
    )

    p_add_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
        verbose_name='Время добавления товара',
    )

    p_price = models.IntegerField(
        default=0,
        null=False,
        blank=True,
        verbose_name='Цена товара',
    )

    p_quantity = models.IntegerField(
        default=0,
        null=False,
        blank=True,
        verbose_name='Количество товара',
    )

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-p_add_date', 'p_quantity', 'p_price']


class ProductsTypes(models.Model):
    p_type = models.IntegerField(
        primary_key=True,
        verbose_name='Тип товара'
    )

    type_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Наименование типа товара'
    )

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Тип товаров'
        ordering = ['p_type']


class ProductsDescription(models.Model):
    p_desc_id = models.IntegerField(
        primary_key=True,
        verbose_name='ID товара'
    )

    p_id = models.OneToOneField(
        Products,
        unique=True,
        on_delete=models.PROTECT
    )

    p_name = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Название товара',
    )

    p_images = models.ImageField(
        upload_to='images/%Y/%m/%d',
        null=False,
        blank=True,
        verbose_name='Изображение товара',
    )

    p_model = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Марка товара',
    )

    p_type = models.ForeignKey(
        ProductsTypes,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    p_size = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Размер обуви',
    )

    p_other_attrs = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Дополнительные аттрибуты',
    )

    class Meta:
        verbose_name = 'Описание товара'
        verbose_name_plural = 'Описание товаров'
        ordering = ['p_desc_id']


class Orders(models.Model):
    o_id = models.IntegerField(
        primary_key=True,
        verbose_name='ID заказа',
    )

    o_name = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='ФИО клиента',
    )

    o_mail = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Электронная почта клиента',
    )

    o_phone = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Телефон клиента',
    )

    delivery_type = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Тип доставки',
    )

    o_create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания заявки',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-o_create_date']


class OrderItems(models.Model):
    oi_id = models.IntegerField(
        primary_key=True,
    )

    o_id = models.ForeignKey(
        Orders,
        null=False,
        blank=True,
        on_delete=models.PROTECT,
    )

    p_id = models.ForeignKey(
        Products,
        null=False,
        blank=True,
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'Связь заказ - товар'
        verbose_name_plural = 'Связь заказы - товары'

class OrdersStatus(models.Model):
    os_id = models.IntegerField(
        primary_key=True,
        verbose_name='ID статуса заказа',
    )

    o_id = models.OneToOneField(
        Orders,
        null=True,
        unique=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    o_status = models.CharField(
        max_length=100,
        choices=[
            ('Заказ создан', 'Заказ создан'),
            ('Заказ оплачен', 'Заказ оплачен'),
            ('Заказ доставлен', 'Заказ доставлен'),
        ],
        default='Заказ создан',
        verbose_name='Статус заказа'
    )

    os_last_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Отслеживание изменения статуса заказа'
    )

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статус заказов'
        ordering = ['os_last_update']
