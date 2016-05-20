from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import CrimeModelTemplate

"""
Serializes geospatial fields from models into GeoJSON data.
"""
class CrimeDataSerializer(GeoFeatureModelSerializer):
    class Meta:
        geo_field = 'geom'
        fields = ('date', 'descriptio', 'group', 'subgroup', 'location', 'latitude', 'longitude')
