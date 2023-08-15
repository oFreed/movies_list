from .models import Movie, Actor, Director, Genre
from .serializers import CreateMovieSerializer, ListMovieSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = ListMovieSerializer
    permission_classes = [
        AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = CreateMovieSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        for movie in serializer.validated_data:
            instance = Movie.objects.create(
                name=movie["name"],
                desc=movie["desc"],
                image_url=movie["image_url"],
                thumb_url=movie["thumb_url"],
                imdb_url=movie["imdb_url"],
                rating=movie["rating"],
                year=movie["year"],
            )

            instance.actors.set(Actor.objects.bulk_create(Actor(name=actor) for actor in movie['actors']))
            instance.genre.set(Genre.objects.bulk_create(Genre(name=actor) for actor in movie['genre']))
            instance.directors.set(Director.objects.bulk_create(Director(name=actor) for actor in movie['directors']))
            instance.save()
        return Response(self.serializer_class(self.queryset, many=True).data, status=status.HTTP_200_OK)
