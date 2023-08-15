from .models import Movie, Actor, Director, Genre
from rest_framework import serializers


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CreateMovieSerializer(serializers.ModelSerializer):
    actors = serializers.ListSerializer(child=serializers.CharField(max_length=100))
    genre = serializers.ListSerializer(child=serializers.CharField(max_length=100))
    directors = serializers.ListSerializer(child=serializers.CharField(max_length=100))

    class Meta:
        model = Movie
        fields = '__all__'


class ListMovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer(many=True)
    directors = DirectorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
