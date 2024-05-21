from django.db import models
from django.contrib.auth.models import AbstractUser


class Roles(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, verbose_name='Роль', null=True)




class Studio(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')

    def __str__(self):
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, verbose_name='Студия', null=True)
    series_col = models.PositiveIntegerField(verbose_name='Серии')
    poster = models.ImageField(verbose_name='Постер', upload_to='aniposters')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

    def to_json(self):
        return {'name': self.name, 'poster': self.poster.url, 'id': self.id}




class Sery(models.Model):
    video = models.FileField()
    name = models.CharField(max_length=300, verbose_name='Название')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(primary_key=True, verbose_name='Номер')

    def __str__(self):
        return self.name





