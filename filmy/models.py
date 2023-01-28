from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)
    movieImg = models.CharField(db_column='movieImg',max_length=800,blank=True,null=True)
    movieName = models.CharField(db_column='movieName',max_length=500,blank=True,null=True)
    movieOverview = models.CharField(db_column='movieOverview',max_length=1000, blank=True,null=True)
    movieRating = models.IntegerField(db_column='movieRating',blank=True,null=True)
    
    def __str__(self):
        return self
    class Meta:
        managed = False
        db_table = 'movie'