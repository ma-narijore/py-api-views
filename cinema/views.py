from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, mixins

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView

from cinema.models import (
    Movie,
    Genre,
    Actor,
    CinemaHall,
)

from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # def list(self, request):
    #     movies = Movie.objects.all()
    #     serializer = MovieSerializer(movies, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def craete(self, request):
    #     serializer = MovieSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def get_object(self, pk):
    #     try:
    #         return Movie.objects.get(pk=pk)
    #     except Movie.DoesNotExist:
    #         raise Http404
    #
    # def retrieve(self, request, pk):
    #     movie = self.get_object(pk)
    #
    #     serializer = MovieSerializer(movie)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def update(self, request, pk):
    #     movie = self.get_object(pk)
    #
    #     serializer = MovieSerializer(movie, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def partial_update(self, request, pk):
    #     movie = self.get_object(pk)
    #
    #     serializer = MovieSerializer(movie, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def destroy(self, request, pk):
    #     movie = self.get_object(pk)
    #
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        genre = self.get_object(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        genre = self.get_object(pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
