# Generated by Django 4.2.11 on 2024-04-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sery',
            name='id',
        ),
        migrations.AddField(
            model_name='sery',
            name='number',
            field=models.PositiveIntegerField(default=1, primary_key=True, serialize=False, verbose_name='Номер'),
            preserve_default=False,
        ),
    ]