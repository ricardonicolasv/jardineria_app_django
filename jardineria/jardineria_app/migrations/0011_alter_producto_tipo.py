# Generated by Django 5.0.6 on 2024-07-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardineria_app', '0010_alter_producto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('FLORES', 'Flores'), ('TIERRA DE HOJA', 'Tierra de hoja'), ('SUCULENTAS', 'Suculentas'), ('MACETEROS', 'Maceteros'), ('OTRO', 'Otro'), ('SUSTRATOS', 'Sustratos')], max_length=25),
        ),
    ]
