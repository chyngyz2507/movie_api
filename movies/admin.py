from django.contrib import admin
from movies.models import Genre, Movie, Review


class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'year',
        'country',
        'slug'
    ]

admin.site.register(Movie, MovieAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'movie',
        'author',
        'text',
        'rating',
        'created_at'
    ]

admin.site.register(Review, ReviewAdmin)
