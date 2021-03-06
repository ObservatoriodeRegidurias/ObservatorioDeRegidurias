# Generated by Django 2.2.13 on 2022-05-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220505_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcercaDeNosotros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen3', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen4', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen5', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen6', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen7', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen8', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('imagen9', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(verbose_name='Acerca de nosotros')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_to', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
