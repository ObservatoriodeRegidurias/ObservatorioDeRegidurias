# Generated by Django 2.2.13 on 2022-04-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220425_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='slug',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='pon el nombre de la noticia'),
        ),
    ]
