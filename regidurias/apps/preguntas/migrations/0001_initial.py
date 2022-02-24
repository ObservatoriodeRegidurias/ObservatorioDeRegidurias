# Generated by Django 2.2.13 on 2022-02-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
                ('asunto', models.CharField(max_length=200)),
                ('comentario', models.TextField()),
                ('resolve', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_to', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
