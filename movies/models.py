from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.URLField()
    genres = models.CharField(max_length=200) 
    overview = models.TextField()
    vote_average = models.FloatField()

    def __str__(self):
        return self.title