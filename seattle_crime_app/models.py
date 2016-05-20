from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class CrimeModel(models.Model):
    eventid = models.CharField(max_length=21)
    description = models.CharField(max_length=254)
    event_date = models.DateTimeField(max_length=254)
    group = models.CharField(max_length=254)
    subgroup = models.CharField(max_length=254)
    offense_num = models.CharField(max_length=15)
    block_location = models.CharField(max_length=254)
    zone_beat = models.CharField(max_length=5)
    longitude = models.FloatField()
    latitude = models.FloatField()



    def __str__(self):
    	return 'Event ID: ' + " " + str(self.eventid) + " " + 'Offense Description: ' + self.description
