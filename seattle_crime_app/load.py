import os
from django.contrib.gis.utils import LayerMapping
from .models import CrimeModel

crime_mapping = {
    #remember 10 character limit
    'cadcdwid': 'cadcdwid',
    'eventnum': 'eventnum',
    'offensenum': 'offensenum',
    'clearance': 'clearance',
    'date': 'date',
    'descriptio': 'descriptio',
    'subgroup': 'subgroup',
    'group': 'group',
    'blocklocat': 'blocklocat',
    'district': 'district',
    'zonebeat': 'zonebeat',
    'location': 'location',
    'longitude': 'longitude',
    'latitude': 'latitude',
    'geom': 'POINT',
}

# Copypaste from geodjango tutorial.
crime_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Seattle_Police_Department_911_Incidents.shp'))

def run(verbose=True):
    lm = LayerMapping(CrimeModel, crime_shp, crime_mapping,
                      transform=False, encoding='utf-8')

    lm.save(strict=True, verbose=verbose)