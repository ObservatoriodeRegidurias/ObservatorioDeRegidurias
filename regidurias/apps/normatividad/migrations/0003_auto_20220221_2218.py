# Generated by Django 2.2.13 on 2022-02-21 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normatividad', '0002_auto_20220221_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normatividad',
            name='entidad',
        ),
        migrations.RemoveField(
            model_name='normatividad',
            name='municipio',
        ),
    ]
