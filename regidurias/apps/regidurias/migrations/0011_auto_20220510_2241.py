# Generated by Django 2.2.13 on 2022-05-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regidurias', '0010_auto_20220505_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regidurias',
            name='correo',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Correo'),
        ),
    ]
