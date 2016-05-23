from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import CrimeModel

"""
Serializes geospatial fields from models into GeoJSON data.
"""

class CrimeDataSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'geom'
        fields = ('cadcdwid', 'eventnum', 'offensenum', 'clearance', 'date', 'descriptio', 'group', 'subgroup', 'location', 'latitude', 'longitude', 'blocklocat', 'district', 'zonebeat')
