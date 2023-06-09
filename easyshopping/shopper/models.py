from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from .db_choices import SHOE_SIZES, MAIN_MATERIALS, SOLE_THICKNESS, TYPES_OF_SOLE, COUNTRIES, SEASONS, CATEGORIES, ORDERS_STATUSES


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
    product_id = models.AutoField(
        primary_key=True,
        verbose_name='ID товара',

    )

    product_name = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Название товара',
    )

    product_code = models.IntegerField(
        default=0,
        null=False,
        blank=True,
        verbose_name='Код товара',
    )

    slug = models.SlugField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Ссылка на товар'
    )

    product_add_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
        verbose_name='Время добавления товара',
    )

    product_price = models.IntegerField(
        default=0,
        null=False,
        blank=True,
        verbose_name='Цена товара',
    )

    product_quantity = models.IntegerField(
        default=0,
        null=False,
        blank=True,
        verbose_name='Количество товара',
    )

    product_rating = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Рейтинг товара'
    )

    category = models.ManyToManyField('Category')

    def __str__(self):
        return f'Товар *{self.product_name}*'

    def get_absolut_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-product_add_date', 'product_quantity', 'product_price']


class ProductsTypes(models.Model):
    product_type = models.AutoField(
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
        ordering = ['product_type']

    def __str__(self):
        return f'{self.type_name}'


class ProductsDescription(models.Model):
    product_desc_id = models.AutoField(
        primary_key=True,
        verbose_name='ID товара'
    )

    product_id = models.ForeignKey(
        Products,
        unique=True,
        on_delete=models.PROTECT
    )

    product_name = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Название товара',
    )

    product_model = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Марка товара',
    )

    product_type = models.ForeignKey(
        ProductsTypes,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name='Тип товара',
    )

    product_size = models.CharField(
        max_length=100,
        choices=SHOE_SIZES,
        null=True,
        blank=True,
        verbose_name='Размер обуви',
    )

    product_other_attrs = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Дополнительные аттрибуты',
    )

    seasons = models.CharField(
        max_length=100,
        choices=SEASONS,
        null=True,
        blank=True,
        verbose_name='Сезонность'
    )

    manufacturer = models.CharField(
        max_length=100,
        choices=COUNTRIES,
        null=True,
        blank=True,
        verbose_name='Страна производитель'
    )

    main_material = models.CharField(
        max_length=100,
        choices=MAIN_MATERIALS,
        null=True,
        blank=True,
        verbose_name='Основной материал'
    )

    sole_thickness = models.IntegerField(
        default=1,
        choices=SOLE_THICKNESS,
        null=True,
        blank=True,
        verbose_name='Толщина подошвы'
    )

    type_of_sole = models.CharField(
        max_length=100,
        choices=TYPES_OF_SOLE,
        null=True,
        blank=True,
        verbose_name='Тип подошвы'
    )

    product_is_hit = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        verbose_name='Хит продаж',
    )

    product_is_on_sale = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        verbose_name='Скидка',
    )

    class Meta:
        verbose_name = 'Описание товара'
        verbose_name_plural = 'Описание товаров'
        ordering = ['product_desc_id']

    def __str__(self):
        return f'{self.product_name}'

class Orders(models.Model):
    order_id = models.AutoField(
        primary_key=True,
        verbose_name='ID заказа',
    )

    order_name = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='ФИО клиента',
    )

    order_mail = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name='Электронная почта клиента',
    )

    order_phone = models.CharField(
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

    order_create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания заявки',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_create_date']


class OrderItems(models.Model):
    order_item_id = models.AutoField(
        primary_key=True,
        verbose_name='ID заказа',
    )

    order_id = models.ForeignKey(
        Orders,
        null=False,
        blank=True,
        on_delete=models.PROTECT,
    )

    product_id = models.ForeignKey(
        Products,
        null=False,
        blank=True,
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'Связь заказ - товар'
        verbose_name_plural = 'Связь заказы - товары'

class OrdersStatus(models.Model):
    order_status_id = models.AutoField(
        primary_key=True,
        verbose_name='ID статуса заказа',
    )

    order_id = models.ForeignKey(
        Orders,
        null=True,
        unique=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    order_status = models.CharField(
        max_length=100,
        choices=ORDERS_STATUSES,
        default='Заказ создан',
        verbose_name='Статус заказа',
    )

    order_status_last_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Отслеживание изменения статуса заказа',
    )

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статус заказов'
        ordering = ['order_status_last_update']


class Category(models.Model):
    category_id = models.AutoField(
        primary_key=True,
        verbose_name = 'ID категории',
    )

    category_name = models.CharField(
        max_length=100,
        choices=CATEGORIES,
        null=False,
        blank=True,
        verbose_name='Название категории',
    )

    def __str__(self):
        return f'Категория {self.category_name}'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Comment(models.Model):
    comment_id = models.AutoField(
        primary_key=True,
        verbose_name = 'ID комментария',
    )

    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Заголокок комментария',
    )

    content = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Текст комментария',
    )

    date_created = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name='Время создания комментария',
    )

    date_edited = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name='Время изменения комментария',
    )

    author_id = models.ForeignKey(
        ShopperUser,
        on_delete=models.PROTECT,
    )

    product_id = models.ForeignKey(
        Products,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'Комментарий от {self.author_id}'


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date_edited', '-date_created']


class ImageProduct(models.Model):
    img_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Название изображения'
    )

    product = models.ForeignKey(
        Products,
        on_delete=models.PROTECT,
    )

    image = models.ImageField(
        upload_to='images/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='Ссылка на изображение',
    )

    default = models.BooleanField(
        default=False,
        verbose_name='Отображается на главной',
    )

    def __str__(self):
        return f'Изображение {self.img_name} товара {self.product}'

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'