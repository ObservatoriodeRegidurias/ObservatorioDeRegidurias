# Generated by Django 2.2.13 on 2022-07-29 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0003_auto_20220728_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariospost',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='commented_posts', to='preguntas.Comentarios'),
        ),
    ]