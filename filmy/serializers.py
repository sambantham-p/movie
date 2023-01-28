from rest_framework import serializers
from filmy.models import Movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields = ('id', 'movieImg', 'movieName', 'movieOverview','movieRating')
        