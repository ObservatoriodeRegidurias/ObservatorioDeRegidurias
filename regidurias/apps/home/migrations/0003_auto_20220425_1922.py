# Generated by Django 2.2.13 on 2022-04-25 19:22

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_observatorio_path_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observatorio',
            name='cabildo_link',
        ),
        migrations.AddField(
            model_name='observatorio',
            name='link_cabildo',
            field=embed_video.fields.EmbedVideoField(default='Some String'),
        ),
    ]