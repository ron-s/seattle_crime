import os
from django.contrib.gis.utils import LayerMapping
from .models import CrimeModel

crime_mapping = {
    #remember 10 character limit
    'cadcdwid': 'CADCDWID',
    'eventnum': 'EventNum',
    'offensenum': 'OffenseNum',
    'eventcode': 'EventCode',
    'date': 'Date',
    'descriptio': 'Descriptio',
    'subgroup': 'SubGroup',
    'group': 'Group',
    'block': 'Block',
    'district': 'District',
    'zonebeat': 'ZoneBeat',
    'census': 'Census',
    'location': 'Location',
    'longitude': 'Longitude',
    'latitude': 'Latitude',
    'geom': 'POINT',
}

# Copypaste from geodjango tutorial.
crime_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Seattle_911.shp'))

def run(verbose=True):
    lm = LayerMapping(CrimeModel, crime_shp, crime_mapping,
                      transform=False, encoding='utf-8')

    lm.save(strict=True, verbose=verbose)