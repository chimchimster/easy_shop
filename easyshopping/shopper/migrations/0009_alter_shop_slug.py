# Generated by Django 3.2.18 on 2023-04-08 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0008_good_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='Ссылка'),
        ),
    ]
