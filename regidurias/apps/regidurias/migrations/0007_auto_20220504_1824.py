# Generated by Django 2.2.13 on 2022-05-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regidurias', '0006_auto_20220427_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regidurias',
            name='genero',
            field=models.CharField(choices=[('1', 'Mujer'), ('2', 'Hombre'), ('3', 'No binario')], default=1, max_length=1, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='regidurias',
            name='telefono',
            field=models.IntegerField(verbose_name='Teléfono'),
        ),
    ]
