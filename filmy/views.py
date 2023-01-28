from django.shortcuts import render
#Allow other domains to access API methods we use decorators CSRF
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

from filmy.models import Movie
from filmy.serializers import MovieSerializer

#API methods

@csrf_exempt
def MovieApi(request,id=0):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movies_serializer = MovieSerializer(movies,many=True)
        #here safe is False to indicate that it is fine even if issues in JSON response.
        return JsonResponse(movies_serializer.data,safe=False)
    
    elif request.method == 'POST':
        movies_data = JSONParser().parse(request)
        movies_serializer = MovieSerializer(data=movies_data)
        if movies_serializer.is_valid():
             movies_serializer.save()
             return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method == 'PUT':
        movies_data = JSONParser().parse(request)
        movies = Movie.objects.get(id = movies_data['id'])
        movies_serializer = MovieSerializer(movies,data=movies_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method == "DELETE":
        movies = Movie.objects.get(id = id)
        movies.delete()
        return JsonResponse("Deleted Successfully",safe=False)