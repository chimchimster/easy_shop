# Generated by Django 3.2.18 on 2023-04-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0015_productsdescription_p_is_hit'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsdescription',
            name='p_is_on_sale',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='productsdescription',
            name='p_is_hit',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Хит продаж'),
        ),
    ]
