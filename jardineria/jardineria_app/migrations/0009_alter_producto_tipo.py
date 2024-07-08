# Generated by Django 5.0.6 on 2024-07-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardineria_app', '0008_alter_producto_tipo_alter_user_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('SUCULENTAS', 'Suculentas'), ('FLORES', 'Flores'), ('TIERRA DE HOJA', 'Tierra de hoja'), ('OTRO', 'Otro'), ('SUSTRATOS', 'Sustratos'), ('MACETEROS', 'Maceteros')], max_length=25),
        ),
    ]
