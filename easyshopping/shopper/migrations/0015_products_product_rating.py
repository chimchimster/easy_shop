# Generated by Django 3.2.18 on 2023-04-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0014_productsdescription_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_rating',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Рейтинг товара'),
        ),
    ]
