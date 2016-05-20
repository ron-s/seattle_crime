import os
from django.contrib.gis.utils import LayerMapping
from .models import CrimeModel

crime_mapping = {
    #remember 10 character limit
    'eventid': 'EventID',
    'eventcode': 'EventCode',
    'descriptio': 'Descriptio',
    'subgroup': 'SubGroup',
    'group': 'Group',
    'date': 'Date',
    'location': 'Location',
    'longitude': 'Longitude',
    'latitude': 'Latitude',
    'wkt': 'WKT',
    'geom': 'POINT', 
}

# Copypaste from geodjango tutorial.
crime_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Seattle_Police_Department_911_Incidents.shp'))

def run(verbose=True):
    lm = LayerMapping(CrimeModel, crime_shp, crime_mapping,
                      transform=False, encoding='utf-8')

    lm.save(strict=True, verbose=verbose)