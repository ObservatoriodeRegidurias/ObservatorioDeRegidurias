# Generated by Django 2.2.13 on 2022-02-21 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto',
            name='entidad',
        ),
        migrations.RemoveField(
            model_name='presupuesto',
            name='municipio',
        ),
    ]
