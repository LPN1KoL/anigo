# Generated by Django 4.2.11 on 2024-04-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0005_alter_anime_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='poster',
            field=models.FileField(upload_to='aniposters', verbose_name='Постер'),
        ),
    ]
