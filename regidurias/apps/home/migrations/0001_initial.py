# Generated by Django 2.2.13 on 2022-01-12 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='carrucel')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_to', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='noticias')),
                ('noticias_link', models.URLField(blank=True, null=True, verbose_name='noticias_link')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_to', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Observatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('cabildo_link', models.URLField(blank=True, null=True, verbose_name='cabildo_link')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_to', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
