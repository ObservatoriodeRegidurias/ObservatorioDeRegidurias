# Generated by Django 2.2.13 on 2022-05-05 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220504_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='slug',
            field=models.CharField(blank=True, default='borrar este campo', max_length=1000, null=True, unique=True),
        ),
    ]
