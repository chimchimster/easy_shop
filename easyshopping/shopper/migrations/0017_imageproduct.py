# Generated by Django 3.2.18 on 2023-04-18 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0016_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название изображения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='Путь до изображения')),
                ('default', models.BooleanField(default=False, verbose_name='Главная для отображения')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopper.products')),
            ],
        ),
    ]
