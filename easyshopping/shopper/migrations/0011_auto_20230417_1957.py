# Generated by Django 3.2.18 on 2023-04-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0010_productsdescription_sole_thickness'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsdescription',
            name='type_of_sole',
            field=models.CharField(blank=True, choices=[('стандартная', 'стандартная'), ('завышеная', 'завышеная'), ('заниженая', 'заниженая')], max_length=100, null=True, verbose_name='Тип подошвы'),
        ),
        migrations.AlterField(
            model_name='productsdescription',
            name='main_material',
            field=models.CharField(blank=True, choices=[('текстиль', 'текстиль'), ('хлопок', 'хлопок'), ('резина', 'резина'), ('кожа', 'кожа'), ('кожзам', 'кожзам'), ('замша', 'замша'), ('велюр', 'велюр'), ('ЭВА', 'ЭВА'), ('искусственная кожа', 'искусственная кожа'), ('искусственная замша', 'искусственная замша'), ('махра', 'махра'), ('мех', 'мех'), ('овечья шерсть', 'овечья шерсть'), ('Оксфорд', 'Оксфорд'), ('ПВХ', 'ПВХ'), ('плюш', 'плюш'), ('полиуретан', 'полиуретан'), ('флис', 'флис')], max_length=100, null=True, verbose_name='Основной материал'),
        ),
    ]
