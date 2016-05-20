from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class CrimeModel(models.Model):
    eventid = models.CharField(max_length=21)
    eventcode = models.IntegerField()
    descriptio = models.CharField(max_length=254)
    subgroup = models.CharField(max_length=254)
    group = models.CharField(max_length=254)
    date = models.DateTimeField(max_length=254)
    location = models.CharField(max_length=254)
    longitude = models.FloatField()
    latitude = models.FloatField()
    wkt = models.CharField(max_length=254)
    geom = models.PointField(srid=-1)


    def __str__(self):
    	return 'Event ID:' + " " + str(self.eventid) + " " + 'Offense Description: ' + self.descriptio
