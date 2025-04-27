from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


class Genre(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        db_table = 'genre_tb'
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='Жанр')
    country = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)


    class Meta:
        db_table = 'movie_tb'
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.reviews.aggregate(avg=Avg('rating'))['avg'] or 0


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='Фильм', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateField(auto_now=True)


    class Meta:
        db_table = 'review_tb'
        verbose_name_plural = 'Обзоры'
        verbose_name = 'Обзор'

    def __str__(self):
        return self.text

    def short_text(self):
        return self.text[:30] + ('...' if len(self.text) > 30 else '')