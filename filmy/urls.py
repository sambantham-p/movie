#root for api methods

from django.urls import  path
from filmy import views

urlpatterns = [
    path('movie/',views.MovieApi),
     path('movie/<int:id>/', views.MovieApi),
  
]