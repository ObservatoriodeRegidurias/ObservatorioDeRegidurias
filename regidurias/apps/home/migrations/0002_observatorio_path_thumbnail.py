# Generated by Django 2.2.13 on 2022-04-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='observatorio',
            name='path_thumbnail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
