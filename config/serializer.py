from rest_framework import serializers

from movies.models import Genre, Movie, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'