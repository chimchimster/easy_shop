# Generated by Django 3.2.18 on 2023-04-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0005_productsdescription_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_slug',
            field=models.SlugField(blank=True, max_length=100, null=True, verbose_name='Ссылка на товар'),
        ),
    ]
