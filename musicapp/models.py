from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    age        = models.IntegerField()
     
    def _str_(self):
        return self.name

class Song(models.Model):  
    title         = models.CharField(max_length=255)
    date_released = models.DateField(default = datetime.today)
    likes         = models.CharField(max_length=255)
    artiste_id    = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    
    def _str_(self):
        return self.name

class Lyrics(models.Model):
    content = models.CharField(max_length=255)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
