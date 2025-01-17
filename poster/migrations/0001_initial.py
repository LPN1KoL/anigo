# Generated by Django 4.2.11 on 2024-04-24 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('series_col', models.PositiveIntegerField(verbose_name='Серии')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Sery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poster.anime')),
            ],
        ),
        migrations.AddField(
            model_name='anime',
            name='studio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poster.studio', verbose_name='Студия'),
        ),
    ]
