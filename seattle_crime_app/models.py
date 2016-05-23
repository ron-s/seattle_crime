from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class CrimeModel(models.Model):
    cadcdwid = models.IntegerField()
    eventnum = models.CharField(max_length=21)
    offensenum = models.IntegerField()
    clearance = models.IntegerField()
    descriptio = models.CharField(max_length=254)
    subgroup = models.CharField(max_length=254)
    group = models.CharField(max_length=254)
    date = models.CharField(max_length=254)
    blocklocat = models.CharField(max_length=254)
    district = models.CharField(max_length=254)
    zonebeat = models.CharField(max_length=254)
    longitude = models.FloatField()
    latitude = models.FloatField()
    location = models.CharField(max_length=254)
    geom = models.PointField(srid=-1)



    # def __str__(self):
    # 	return 'Event ID: ' + " " + str(self.eventid) + " " + 'Offense Description: ' + self.description

    def __str__(self):
        return 'Offense Number:' + " " + str(self.offensenum) + " " + 'Offense Type: ' + self.descriptio
