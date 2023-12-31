# Generated by Django 4.2.3 on 2023-07-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_implementos_precio_alter_maquinaria_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementos',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='maquinaria',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='suplementos',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
