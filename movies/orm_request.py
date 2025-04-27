from django.db.models import Avg, Count
from django.contrib.auth import get_user_model
from movies.models import Genre, Movie, Review

#Получи топ-3 фильма с наибольшим количеством отзывов.
top_movies = Movie.objects.annotate(num_reviews=Count('Фильм')).order_by('-num_reviews')[:3]
for movie in top_movies:
    print(movie.title, movie.num_reviews)

#Выведи средний рейтинг каждого фильма.
movies = Movie.objects.annotate(avg_rating=Avg('Фильм__rating'))
for movie in movies:
    print(f"{movie.title} — средний рейтинг: {movie.avg_rating}")

#Найди все фильмы, в которых есть жанр “Драма”.
drama_movies = Movie.objects.filter(genres__name='Драма')
for movie in drama_movies:
    print(movie.title)

#Получи все отзывы пользователя с username = 'user1', отсортированные по дате.
User = get_user_model()
user = User.objects.get(username='Алымкул')

reviews = Review.objects.filter(author=user).order_by('-created_at')

for review in reviews:
    print(f"{review.movie.title} — {review.rating} — {review.created_at}")

#Получи все фильмы, у которых средний рейтинг выше 7.
movies = Movie.objects.annotate(avg_rating=Avg('фильм__rating')).filter(avg_rating__gt=7)

for movie in movies:
    print(f"{movie.title} — средний рейтинг: {movie.avg_rating}")

#Получи все жанры и количество фильмов в каждом (используй annotate).
genres = Genre.objects.annotate(movie_count=Count('Жанр'))

for genre in genres:
    print(f"{genre.name}: {genre.movie_count} фильм(ов)")

#Получи список стран, из которых есть хотя бы один фильм (уникальные значения).
countries = Movie.objects.values_list('country', flat=True).distinct()

for country in countries:
    print(country)

# Выведи все фильмы, у которых нет ни одного отзыва.
movies_without_reviews = Movie.objects.annotate(review_count=Count('Фильм')).filter(review_count=0)

for movie in movies_without_reviews:
    print(movie.title)