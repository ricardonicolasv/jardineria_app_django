# Generated by Django 5.0.6 on 2024-07-09 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardineria_app', '0009_alter_producto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('OTRO', 'Otro'), ('SUSTRATOS', 'Sustratos'), ('SUCULENTAS', 'Suculentas'), ('FLORES', 'Flores'), ('TIERRA DE HOJA', 'Tierra de hoja'), ('MACETEROS', 'Maceteros')], max_length=25),
        ),
    ]
